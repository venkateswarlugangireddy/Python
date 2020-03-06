from collections import defaultdict
import boto3
import datetime
import csv
import operator
import os


ec2 = boto3.resource('ec2')

running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

fieldnames = ['ID', 'Name', 'Type', 'State', 'Launch Time', 'AMI']
with open('dicttocsv.csv', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for instance in running_instances:
        for tag in instance.tags:
          if 'Name'in tag['Key']:
            name = tag['Value']

        writer.writerow({'ID': instance.id, 'Name': name, 'Type': instance.instance_type,
         'State': instance.state['Name'], 'Launch Time': instance.launch_time, 'AMI': instance.image_id})

    csv_file.close()

data = csv.reader(open('dicttocsv.csv'),delimiter=',')
#next(data)
sortedlist = sorted(data, key=operator.itemgetter(4))   
#now write the sorte result into new CSV file
with open("dicttocsv.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    fileWriter.writerow(fieldnames)
    for row in sortedlist:
        fileWriter.writerow(row)
