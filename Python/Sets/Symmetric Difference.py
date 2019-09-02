m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
output = list(M ^ N)
output.sort()
for out in output:
    print(out)
