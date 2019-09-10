count = 1
while count < 10:
  if count % 2 == 0:
    #count += 1
    break
  print("number is odd : %s" %count)
  count += 1


ages = dict([('ven', '32'), ('swe', '26')])
for x,y in ages.items():
  print(f"name is: {x}")
  print(f"age is: {y}")
  


