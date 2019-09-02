s = input()
one, two, three, four, five = "False", "False", "False", "False", "False"
for i in range(len(s)):
    if (s[i].isalnum()):
        one = "True"
    if (s[i].isalpha()):
        two = "True"
    if (s[i].isdigit()):
        three = "True"
    if (s[i].islower()):
        four = "True"
    if (s[i].isupper()):
        five = "True"
print(one)
print(two)
print(three)
print(four)
print(five)
