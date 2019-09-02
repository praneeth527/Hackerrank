import numpy as np

N, M = list(map(int, input().split()))
A, B = [], []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

A = np.array(A)
B = np.array(B)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
