import boto4
client = boto3.client('ec2')
response = client.run_instances(
     ImageId='ami-068e0f1a600cd311c',
     InstanceType='t2.micro',
     KeyName='public',
     MaxCount=1,
     MinCount=1

)


