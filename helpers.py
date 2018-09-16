import boto3

from config import S3_ACCESS_KEY, S3_SECRET_KEY

s3 = boto3.client(
 's3',
 aws_access_key_id=S3_ACCESS_KEY,
 aws_secret_access_key=S3_SECRET_KEY,
)

#s3 = boto3.client("s3")