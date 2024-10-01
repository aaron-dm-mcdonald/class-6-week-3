# Import the boto3 library, AWS SDK for Python
# NOTE: Must have CLI utility configured for authentication 
import boto3 

# Create an EC2 client using boto3, specifying the AWS region
ec2_client = boto3.client('ec2', region_name="us-east-2")

# Describe all the volumes in the specified region
volumes = ec2_client.describe_volumes()



# Print the list of volumes
print(volumes['Volumes'])
