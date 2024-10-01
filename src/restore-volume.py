from operator import itemgetter
import boto3

# Define the AWS region
region = 'eu-west-3'

# Create EC2 client and resource
ec2_client = boto3.client(
    'ec2',
    region_name=region
)
ec2_resource = boto3.resource(
    'ec2',
    region_name=region
)

# Specify the instance ID
instance_id = 'i-02078856a347e1079'

# Describe volumes attached to the specified instance
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

# Get the first volume attached to the instance
instance_volume = volumes['Volumes'][0]

# Describe snapshots for the instance volume
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

# Sort snapshots by StartTime in descending order and get the latest snapshot
latest_snapshot = sorted(
    snapshots['Snapshots'],
    key=itemgetter('StartTime'),
    reverse=True
)[0]

# Create a new volume from the latest snapshot
new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot["SnapshotId"],
    AvailabilityZone=instance_volume["AvailabilityZone"],
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                },
            ]
        },
    ]
)

# Loop until the new volume becomes available
while True:
    # Describe the status of the new volume
    volume_status = ec2_client.describe_volumes(
        VolumeIds=[new_volume["VolumeId"]]
    )
    
    # Print the current state of the volume
    print(volume_status["Volumes"][0]["State"])
    
    # Check if the volume is available
    if volume_status["Volumes"][0]["State"] == "available":
        # Print the final state of the volume
        print(volume_status["Volumes"][0]["State"])
        
        # Attach the new volume to the instance
        ec2_resource.Instance(instance_id).attach_volume(
            Device='/dev/xvdb',
            VolumeId=new_volume["VolumeId"]
        )
        break  # Exit the loop once the volume is attached

