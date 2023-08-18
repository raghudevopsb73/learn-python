import boto3
from botocore.exceptions import ClientError
import json
from tabulate import tabulate
from prettytable import PrettyTable

ec2 = boto3.client('ec2', region_name='us-east-1')

# instance_list = []
# out = ec2.describe_instances()["Reservations"]
# #print(out)
#
# for instances in out:
#     for instance in instances["Instances"]:
#         instance_list.append([instance["InstanceId"], instance["PrivateIpAddress"], instance["InstanceType"] ])
#
#         # instance_list.append(tabulate([
#         #     [instance["InstanceId"], instance["PrivateIpAddress"], instance["InstanceType"] ],
#         # ], tablefmt='orgtbl'))
# print(tabulate(instance_list, tablefmt='orgtbl'))

t = PrettyTable(['InstanceID', 'PrivateIP', 'InstanceType'])
out = ec2.describe_instances()["Reservations"]
t.align["InstanceID"] = "l"
t.align["PrivateIP"] = "l"
t.align["InstanceType"] = "l"
for instances in out:
    for instance in instances["Instances"]:
        t.add_row([instance["InstanceId"], instance.get["PrivateIpAddress", "-"], instance.get["InstanceType", "-"] ])


with open('/usr/share/nginx/html/sample.txt', 'w') as w:
    w.write(str(t))