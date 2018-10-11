name = raw_input("Please enter your name: ")
age = int(input("Please enter your age: "))

import datetime
year_now = datetime.date.today().year

year = str(year_now + (100 - age))

print ("Hi %s ! you are gonna be 100 years in the year %s" %(name,year))
print (name + " will be 100 years in " + year )
print (2 * "test")