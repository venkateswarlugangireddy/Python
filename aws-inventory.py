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


'''
ec2info = defaultdict()
for instance in running_instances:
    print(type(instance))
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    
    # Add instance info to a dictionary       
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time,
        'AMI': instance.image_id
        }

with open('instance_inventory.csv', mode='w') as instance_inventory:
    instance_writer = csv.writer(instance_inventory, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    print(name)

print(instance_inventory)

print(ec2info)
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time', 'AMI']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
'''
