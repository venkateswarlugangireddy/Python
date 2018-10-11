
num = int(input("please enter the number: "))
x = range(1, num+1 )
y=[]
for i in x:
    if num % i == 0:
        y.append(i)

print y