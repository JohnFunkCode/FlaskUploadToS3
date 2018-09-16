s3 = boto3.resource('s3')
data = open('config.py','rb')
s3.Bucket('jpf-python-datastore').put_object(Key='config.py', Body=data)

s4=boto3.client('s3')
data = open('config.py','rb')
s4.upload_fileobj( data,'jpf-python-datastore','one.py')

s5 = boto3.client('s3',aws_access_key_id='YourAccessKeyHere',aws_secret_access_key='YourSecretKeyHere'
                  )
data = open('config.py','rb')
s5.upload_fileobj( data,'jpf-python-datastore','two.py')

