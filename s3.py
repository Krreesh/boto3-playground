import boto3
#import uuid
import json

bucket_name = 'krathena'

bucket_policy ={
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "statement2",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::449602167449:user/asmita"
         },
         "Action": [
             "s3:GetObject"
         ],
         "Resource": [
            "arn:aws:s3:::krathena/*"
         ]
      }
   ]
}

bucket_policy = json.dumps(bucket_policy)

s3 = boto3.client('s3')

response= s3.download_file(bucket_name, '640137311585_CloudTrail.json', 'myfile.csv')
#response = s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
#response = s3.delete_bucket_policy(Bucket=bucket_name)

print(response)