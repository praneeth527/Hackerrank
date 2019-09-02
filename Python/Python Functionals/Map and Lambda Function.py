cube = lambda x: pow(x, 3)


def fibonacci(n):
    if (n < 1):
        return []
    if (n == 1):
        return [0]
    l = [0] * n
    l[0], l[1] = 0, 1
    for i in range(2, n):
        l[i] = l[i - 1] + l[i - 2]
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
