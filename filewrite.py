
numbers = [1, 2, 3, 4]

f = open("test.txt", "w")
for i in numbers:
    f.write(str(i) + "\n")
f.close()

g = open("test.txt", "a+")
for i in [5, 6, 7]:
    g.write(str(i) + "\n")
g.seek(0)
g.read()
g.close()

