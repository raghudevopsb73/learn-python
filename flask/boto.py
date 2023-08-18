import boto3
from botocore.exceptions import ClientError
import json
from tabulate import tabulate



ec2 = boto3.client('ec2', region_name='us-east-1')

out = ec2.describe_instances()["Reservations"]
#print(out)
for instance in out:
    for ami in instance["Instances"]:
        #print(ami["ImageId"])
        print(tabulate([['InstanceID', ami["InstanceId"]], ['Bob', 19]], tablefmt='orgtbl'))
