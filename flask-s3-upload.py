from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
import boto3
from cfenv import AppEnv

env=AppEnv()
print env.name
print env.port
s3bucket = env.get_service(name='s3bucket')
print s3bucket.credentials


app = Flask(__name__)
#app.config.from_object("config.config")




#from .helpers import *

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/")
def index():
    # print "S3_BUCKET: " + app.config["S3_BUCKET"]
    # print "S3_ACCESS_KEY: " + app.config["S3_ACCESS_KEY"]
    # print "S3_SECRET_KEY: " + app.config["S3_SECRET_KEY"]
    # print "S3_LOCATION: " + app.config["S3_LOCATION"]

#    print s3

    return render_template("index.html")

def upload_file_to_s3(file, bucket_name, acl="public-read"):

    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                 "ACL": acl,
                 "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Bad Happened: ", e)
        print file
        print bucket_name
        print acl
        print file.content_type
        return e

    return "{}{}".format(S3_LOCATION, file.filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST"])
def upload_file():
    # A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

    # B
    file    = request.files["user_file"]

    """
        These attributes are also available
    
        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype
    
    """

    # C.
    if file.filename == "":
        return "Please select a file"

    # D.
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
    #        output = upload_file_to_s3(file, app.config["S3_BUCKET"])
        output = upload_file_to_s3(file, S3_BUCKET)
        return '<html><a href="' + str(output) + '">'+ str(output) +'</a></html>'

    else:
        return redirect("/")


if __name__ == '__main__':
    env = AppEnv()
    print "env.name: "+ env.name
    print "env.port: "+ str(env.port)
    s3bucket = env.get_service(name='s3bucket')
    creds = s3bucket.credentials
    print "env.creds.bucket: "+creds['S3_BUCKET']
    print "env.creds.ACCESS_KEY"+creds['S3_ACCESS_KEY']
    print "env.creds.ACCESS_KEY"+creds['S3_SECRET_KEY']

    S3_BUCKET=creds['S3_BUCKET']
    S3_ACCESS_KEY=creds['S3_ACCESS_KEY']
    S3_SECRET_KEY=creds['S3_SECRET_KEY']
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

    print "S3_BUCKET: " + S3_BUCKET
    print "S3_ACCESS_KEY: " + S3_ACCESS_KEY
    print "S3_SECRET_KEY: " + S3_SECRET_KEY
    print "S3_LOCATION: " + S3_LOCATION

    s3 = boto3.client(
        's3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )


    port = int(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=port)