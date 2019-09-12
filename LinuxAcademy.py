'''

#Exercise: Creating and Displaying Variables
first_name = "venkat"
last_name = "g"
age = 31
birth_date = "06-04-89"

print("my name is %s %s" %(first_name,last_name))
print("I was born in %s and I'm %s years old." %(birth_date, age))

#Working with If/Else
user = { 'admin': True, 'active': True, 'name': 'Kevin' }

prefix = ""

if user['admin'] and user['active']:
  prefix = "ACTIVE -(ADMIN)"
elif user['admin']:
  prefix = "(ADMIN)"
elif user['active']:
  prefix = "ACTIVE"

print(prefix + user['name'])


import sys
print(f"file name {sys.argv[0]}")
#print("first argument %s" % sys.argv[1])

########
import json
import os
import random

count = int(os.getenv("File_Count") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
  amount = random.uniform(1.00, 1000)
  content = {
    'topic': random.choice(words),
    'amount': "%.2f" % amount
  }
  with open(f"./new/recipt-{identifier}.json", 'w') as f:
    json.dump(content, f)


message = input("please enter the message: ")
count = input("enter the count value: ").strip()

if count:
  count = int(count)
else:
  count = 1

def echo_fun(message, count):
  while count >= 1:
    print(message)
    count -= 1

echo_fun(message, count)

'''
'''
def get_file_name():
  file_name=input("please enter file name")
  return file_name

file_name = get_file_name()

print(file_name)

with open(file_name, 'w') as f:
  eof = False
  lines=[]

  while not eof:
    line=input()
    if line.strip():
      lines.append(f"{line}\n")
    else:
      eof = True

  f.writelines(lines)
  
'''
'''
import argparse

parser = argparse.ArgumentParser(description='test file')
parser.add_argument('file_name', help="file name")
parser.add_argument('line_number', type=int, help='line number')
args = parser.parse_args()

try:
  lines = open(args.file_name, 'r').readlines()
  line = lines[args.line_number - 1]
except IndexError:
  print("line index error")
else:
  print(line)
  '''

  