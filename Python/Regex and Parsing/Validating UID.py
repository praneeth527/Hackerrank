import re


def validateUID(string):
    string = ''.join(sorted(string))
    if (re.search(r"[A-Z]{2,}", string) and re.search(r"[0-9]{3,}", string) and not re.search(
            r"[^a-zA-Z0-9]", string) and not re.search(r"(.)\1", string) and len(string) == 10):
        print("Valid")
    else:
        print("Invalid")


for _ in range(int(input())):
    validateUID(input())
