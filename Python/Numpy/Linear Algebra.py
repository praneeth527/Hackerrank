import numpy as np

A = []
for _ in range(int(input())):
    A.append(list(map(float, input().split())))
A = np.array(A)

print(round(np.linalg.det(A), 2))
