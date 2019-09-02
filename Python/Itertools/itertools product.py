from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
out = (list(product(A, B)))
for i in out:
    print(i, end=' ')
