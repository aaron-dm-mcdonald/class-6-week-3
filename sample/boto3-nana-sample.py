# sample/boto3-nana-sample.py
# Import the boto3 library, AWS SDK for Python
# Note: Must have CLI utility configured for authentication 
#------------------------------------------------------------------
import boto3 


# Create an EC2 client using boto3, specifying the AWS region
# Note: this is essenitally boilerplate code, however keep in mind the ec2_client is what will "talk" to AWS EC2 for us (more precisely, it will handle API calls)
ec2_client = boto3.client('ec2', region_name="us-east-2")

# Describe all the volumes in the specified region
# Here we use Boto3's describe_volume's function and the ec2_client to retrieve data from our volumes
# The retrieved data is stored in 'volumes' (as a dictionary)
volumes = ec2_client.describe_volumes()


# Print the list of volumes
# Since volumes is a 'dictionary' (ordered list with key-value pairs) we use the key 'Volumes' to specify we want data about the volumes. 
print(volumes['Volumes'])
