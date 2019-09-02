for _ in range(int(input())):
    nums = input().split()
    try:
        print(int(nums[0]) // int(nums[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
