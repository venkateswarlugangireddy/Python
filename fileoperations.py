f=open("fruits.txt")
fruits=f.read()
f.close()
content=fruits.splitlines()
for i in content:
    print(len(i))


f=open("fruits.txt")
content=f.readlines()
content=[line.strip() for line in content]
f.close()
for i in content:
    print i
