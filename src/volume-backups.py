import boto3
import schedule

region = 'us-east-2'
ec2_client = boto3.client(
    'ec2',
    region_name=region
)

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

# print(volumes['Volumes'])

def create_volume_snapshots():
    for volume in volumes['Volumes']:
        try:
            new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId']
            )
            print(new_snapshot)
        except:
            pass


schedule.every(5).days.do(create_volume_snapshots)

while True:
    schedule.run_pending()
