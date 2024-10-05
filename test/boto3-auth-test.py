# sample/boto3-auth-test.py
# This script demonstrates how to authenticate with AWS using the boto3 library.
# Before running this script, make sure you have the AWS CLI configured for authentication.

#------------------------------------------------------------------

import boto3  # Import the boto3 library, the AWS SDK for Python
from botocore.exceptions import NoCredentialsError, PartialCredentialsError  # Import specific exceptions for handling errors

#------------------------------------------------------------------

# Create a session using your AWS credentials from the configured profile
session = boto3.Session()

# Create an IAM (Identity and Access Management) client to interact with IAM services
iam_client = session.client('iam')

#------------------------------------------------------------------

# Define a authentication function 
def verify_authentication():
    try:
        # List IAM users to verify authentication
        response = iam_client.list_users()
        
        # Print a success message if authentication is successful
        print("Authentication successful. Here are your IAM users:")
        
        # Iterate through the list of users and print their usernames
        for user in response['Users']:
            print(f"  - {user['UserName']}")
    
    # Handle the case where no AWS credentials are found
    except NoCredentialsError:
        print("Error: No credentials found. Please configure your AWS CLI credentials.")
    
    # Handle the case where the provided credentials are incomplete
    except PartialCredentialsError:
        print("Error: Incomplete credentials provided. Please check your configuration.")
    
    # Handle any other exceptions that might occur
    except Exception as e:
        print(f"An error occurred: {e}")


#------------------------------------------------------------------

# Call the function to verify authentication
verify_authentication()  


