

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("please enter the number: "))
x = []
for i in a:
    if i < num:
        x.append(i)
print x


y=[i for i in a if i < num]
print y