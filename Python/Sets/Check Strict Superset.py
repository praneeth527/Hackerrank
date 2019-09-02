A = set(map(int, input().split()))
n = int(input())
flag = True
for i in range(n):
    B = set(map(int, input().split()))
    flag = (A.issuperset(B) and len(A - B) >= 1)
    if (not flag):
        break
print(flag)
