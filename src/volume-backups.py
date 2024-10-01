# volume-backups.py
#------------------------------------------------------------------
import boto3
import schedule

# Boilderplate 
# Define the AWS region
region = 'us-east-2'

# Create an EC2 client
ec2_client = boto3.client(
    'ec2',
    region_name=region
)


#------------------------------------------------------------------


# Describe volumes with the tag 'Name' set to 'prod'
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            "Values": ["prod"]
        }
    ]
)

#------------------------------------------------------------------
# Uncomment the following line to print the volumes for debugging
# print(volumes['Volumes'])
#------------------------------------------------------------------

def create_volume_snapshots():
    # Iterate over each volume
    for volume in volumes['Volumes']:
        try:
            # Create a snapshot for the current volume
            new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId']
            )
            # Print the details of the new snapshot
            print(new_snapshot)
        except Exception as e:
            # Handle any exceptions that occur
            print(f"An error occurred: {e}")
            pass

#------------------------------------------------------------------


# Schedule the snapshot creation to run every 5 days
schedule.every(5).days.do(create_volume_snapshots)

# Continuously run the scheduled tasks
while True:
    schedule.run_pending()
