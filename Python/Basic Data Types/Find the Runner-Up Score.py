n = int(input())
arr = input()
s = []
li = arr.split()
print
for i in li:
    s.append(int(i))
s.sort()
k = len(s)
i = s.count(s[k - 1])
print(s[k - i - 1])
