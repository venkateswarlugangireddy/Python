
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
