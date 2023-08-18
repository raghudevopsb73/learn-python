import boto3
from botocore.exceptions import ClientError
import json


ec2 = boto3.client('ec2', region_name='us-east-1')

out = ec2.describe_instances()["Reservations"]["Instances"][0]
print(out)
