import boto3

ec2_client = boto3.client('ec2', region_name="us-east-2")

volumes = ec2_client.describe_volumes()
print(volumes['Volumes'])