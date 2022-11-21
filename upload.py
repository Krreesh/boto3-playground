import boto3
import logging
from botocore.exceptions import ClientError
import os

def upload(filename, bucket, key=None):
    """ Upload a file to bucket
    :param filename
    
    """
    if key is None:
        key = os.path.basename(filename)
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket, key)
    except ClientError as  e:
        logging.error(e)
        return False
    return True

def upload_binary(filename, bucket, key=None):
    if key is None:
        key = os.path.basename(filename)
    s3 = boto3.client('s3')
    with open(filename, 'rb') as f:
        s3.upload_fileobj(f, bucket, key)
        
#upload('s3.py', 'krathena')
upload_binary ('/home/ec2-user/environment/js-sdk/static-website-example-master.zip', 'krathena')