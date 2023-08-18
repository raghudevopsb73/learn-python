import boto3
from botocore.exceptions import ClientError
import json
from tabulate import tabulate



ec2 = boto3.client('ec2', region_name='us-east-1')
instance_list = []
out = ec2.describe_instances()["Reservations"]
#print(out)
for instances in out:
    for instance in instances["Instances"]:
        instance_list.append([instance["InstanceId"], instance["PrivateIpAddress"], instance["InstanceType"] ])

        # instance_list.append(tabulate([
        #     [instance["InstanceId"], instance["PrivateIpAddress"], instance["InstanceType"] ],
        # ], tablefmt='orgtbl'))
print(tabulate(instance_list, tablefmt='orgtbl'))
