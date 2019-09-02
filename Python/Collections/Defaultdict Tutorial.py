from collections import defaultdict

n, m = list(map(int, input().split()))
A = defaultdict(list)
for i in range(1, n + 1):
    A[input()].append(i)
for i in range(m):
    key = input()
    if (len(A[key]) > 0):
        print(*A[key])
    else:
        print(-1)
