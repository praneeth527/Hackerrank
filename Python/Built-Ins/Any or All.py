N = int(input())
nums = list(map(int, input().rstrip().split()))
print(all(i > 0 for i in nums) and any(str(i) == str(i)[::-1] for i in nums))
