##This will delete unused security groups
import sys
import argparse
import boto3

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--profile', type=str, required=True, help='provide AWS profile name')
my_parser.add_argument('--dry-run', action='store_true')

args = my_parser.parse_args()
print(args.profile)
print(args.dry_run)


session = boto3.Session(profile_name=args.profile)
ec2 = session.client('ec2', region_name='us-west-2')

all_sgs=[]
using_sgs=[]

sg=ec2.describe_security_groups()
for name in sg['SecurityGroups']:
  if name['GroupName']!= 'default' and not name['GroupName'].startswith('AWS-OpsWorks-'):
    all_sgs.append(name['GroupName'])

eni=ec2.describe_network_interfaces()
#print(eni)
for name in eni['NetworkInterfaces']:
  if len(name['Groups'])!=0:
    if name['Groups'][0]['GroupName'] not in using_sgs and name['Groups'][0]['GroupName'] != 'default':
      using_sgs.append(name['Groups'][0]['GroupName'])

unused_sgs = [r for r in all_sgs if r not in using_sgs]

for i in unused_sgs:
  if args.dry_run == True:
    print(unused_sgs)
  else:
    ec2.delete_security_group(GroupName=i, DryRun=True)

print(len(unused_sgs))
# print(unused_sgs)
# print(len(all_sgs))
# print(len(using_sgs))