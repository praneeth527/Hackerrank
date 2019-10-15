n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happinessCount = 0

for num in arr:
    if num in A:
        happinessCount += 1
    if num in B:
        happinessCount -= 1

print(happinessCount)
