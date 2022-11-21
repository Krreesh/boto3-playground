import logging, boto3
from botocore.exceptions import ClientError
from botocore.client import Config

def create_url(bucket, key, expiration=3600):
    """ This generates presigned url with temporary credentials
    
    """
    s3 = boto3.client('s3', aws_access_key_id='AKIAZKCZIGVQZLOUMME4', aws_secret_access_key='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', config=Config(region_name='ap-south-1', signature_version='s3v4'))
    try:
        url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
    return url

new_url = create_url('krathena', 'static-website-example-master.zip', 1200)
print("You got url")
print(new_url)