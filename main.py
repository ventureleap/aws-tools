import boto3
import csv
import sys

client = boto3.client('route53')

hosted_zone_id = str(sys.argv[1])


def makeEntry(name, type, value):
    print(r'Making entry for ' + name + ' of type ' + type + ' with value ' + value + '\n')
    client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Comment': 'Venture Leap - AWS Route53 Tools',
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': type,
                        'TTL': 600,
                        'ResourceRecords': [
                            {
                                'Value': value
                            }
                        ]
                    }
                }
            ]
        }
    )


with open('entries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        makeEntry(row[0], row[1], row[2])
