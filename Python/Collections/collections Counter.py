from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())
sum = 0
shoe_sizes_counter = Counter(shoe_sizes)
for i in range(N):
    x, value = list(map(int, input().split()))
    if shoe_sizes_counter[x] > 0:
        shoe_sizes_counter[x] -= 1
        sum += value
print(sum)
