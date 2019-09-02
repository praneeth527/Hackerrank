import numpy as np

arr = list(map(int, input().split()))
a = np.array(arr)
# or
# a.shape=(3,3)
# print(a)
print(np.reshape(a, (3, 3)))
