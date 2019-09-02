import numpy as np

N, M, P = list(map(int, input().split()))
a1, a2 = [], []
for _ in range(N):
    a1.append(list(map(int, input().split())))
for _ in range(M):
    a2.append(list(map(int, input().split())))

arr1 = np.array(a1)
arr2 = np.array(a2)

print(np.concatenate((arr1, arr2), axis=0))
