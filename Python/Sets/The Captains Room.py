from collections import Counter

n = int(input())
R = list(map(int, input().split()))
counterR = Counter(R)

for room, rep in counterR.items():
    if (rep == 1):
        print(room)
        break
