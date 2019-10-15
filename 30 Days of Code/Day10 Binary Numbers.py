# def binary(n):
#     b = ''
#     while n > 0:
#         b += str(n % 2)
#         n = n // 2
#     return b[::-1]

# use above method or built in method in python bin(number)

def findSeq(s):
    if '1' not in s:
        return 0
    else:
        max = 1
        i = 0
        while (i < len(s) - 1):
            count = 1
            while s[i] == '1' and s[i + 1] == '1':
                i += 1
                count += 1
                if (i + 1 == len(s)):
                    break
            if (count > max):
                max = count
            i += 1
        return max


print(findSeq(str(bin(int(input())))))
