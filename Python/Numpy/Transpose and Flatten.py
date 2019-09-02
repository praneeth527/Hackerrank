import numpy as np

N, M = list(map(int, input().split()))
l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
arr = np.array(l)
print(np.transpose(arr))
print(arr.flatten())
