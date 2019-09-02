nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
res = list(map(str, a[d:] + a[:d]))
print(' '.join(res))
