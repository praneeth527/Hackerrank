from collections import deque

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    le = len(l)
    while (i < le - 1 and l[i] >= l[i + 1]):
        i += 1
    while (i < le - 1 and l[i] <= l[i + 1]):
        i += 1
    if (i == le - 1):
        print("Yes")
    else:
        print("No")
