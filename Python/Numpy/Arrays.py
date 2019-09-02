import numpy


def arrays(arr):
    arr = arr[::-1]
    return numpy.array(arr, float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
