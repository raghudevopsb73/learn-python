import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

ec2.run_instances(
    ImageId='ami-03265a0778a880afb',
    InstanceType='t3.small',
    SecurityGroupIds=["sg-08b043c018c643809"],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'test'
                },
            ]
        },
    ]
)
