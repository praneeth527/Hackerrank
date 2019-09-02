n = int(input())
li = []
s = []
na = []
for i in range(n):
    name = input()
    score = float(input())
    li.extend([[name, score]])

for i in range(len(li)):
    s.append(li[i][1])
s.sort()
slow = s[0]
for i in s:
    if (i != slow):
        slow = i
        break
for i in li:
    if (i[1] == slow):
        na.append(i[0])
na.sort()

for i in na:
    print(i)
