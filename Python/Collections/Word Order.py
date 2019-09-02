from collections import OrderedDict,Counter
n=int(input())
l=list()
for i in range(n):
    l.append(input())
counter=Counter(l)
print(len(counter))
print(*Counter(counter).values())
