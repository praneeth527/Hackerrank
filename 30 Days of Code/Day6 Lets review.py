def seperateStrings(string):
    even, odd = '', ''
    for i in range(0, len(string), 2):
        even += string[i]
    for i in range(1, len(string), 2):
        odd += string[i]
    print(even, odd)


for _ in range(int(input())):
    seperateStrings(input())
