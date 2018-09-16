from flask import Flask, render_template, request, redirect
import os


S3_BUCKET                 = 'jpf-python-datastore'
S3_ACCESS_KEY             = 'access-key'
S3_SECRET_KEY             = 'secret-key'
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

app = Flask(__name__)
port = int(os.getenv("PORT"))


@app.route("/")
def index():
    print "S3_BUCKET: " + S3_BUCKET
    print "S3_ACCESS_KEY: " + S3_ACCESS_KEY
    print "S3_SECRET_KEY: " + S3_SECRET_KEY
    print "S3_LOCATION: " + S3_LOCATION


    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)