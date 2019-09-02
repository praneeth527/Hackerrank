import numpy as np

N, M = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A = np.array(A)
print(np.prod(np.sum(A, axis=0)))
