# cleanup-snapshot.py
#------------------------------------------------------------------
import boto3
from operator import itemgetter

# Define the AWS region
region = 'eu-west-3'

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
            "Values": [
                "prod"
            ]
        }
    ]
)


#------------------------------------------------------------------
# Iterate over each volume
for volume in volumes['Volumes']:

    # Describe snapshots for the current volume
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )
    
    # Sort snapshots by StartTime in descending order
    sorted_by_date = sorted(
        snapshots['Snapshots'],
        key=itemgetter('StartTime'),
        reverse=True
    )


#------------------------------------------------------------------
    
    # Uncomment the following lines to print snapshot start times before and after sorting
    # for snapshot in snapshots['Snapshots']:
    #     print(snapshot['StartTime'])
    
    # print("-" * 50)
    # for snapshot in sorted_by_date:
    #     print(snapshot['StartTime'])
#------------------------------------------------------------------

    
# Delete all but the two most recent snapshots
for snapshot in sorted_by_date[2:]:
    response = ec2_client.delete_snapshot(
        SnapshotId=snapshot['SnapshotId']
    )
    print(response)

