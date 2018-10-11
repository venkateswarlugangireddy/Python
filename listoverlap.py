a = range(1,10)
b = range(2,14)
y=[]
for i in a:
    if i in b:
        y.append(i)

print y

print set(a) & set(b)