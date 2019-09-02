lis = []
n = int(input())
for i in range(n):
    li = input()
    data = li.split()
    lis.extend([data])

name = input()
for i in lis:
    if (i[0] == name):
        avg = float(i[1]) + float(i[2]) + float(i[3])
        val = avg / 3
print("{0:.2f}".format(val))
