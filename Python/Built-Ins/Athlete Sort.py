N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())

outList = sorted(arr, key=lambda x: x[K])

for out in outList:
    print(*out)
