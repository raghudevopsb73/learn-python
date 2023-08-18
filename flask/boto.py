import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='us-east-1')

out = ec2.describe_instances()
print(out)
