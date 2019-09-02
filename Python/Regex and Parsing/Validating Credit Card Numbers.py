import re


def validateCreditCard(string):
    if (not re.search(r"^[456]", string)):
        return False
    if (re.search(r"[^-0-9]", string)):
        return False
    if (re.search(r"^[0-9]*$", string)):
        if (len(string) != 16):
            return False
    if (re.search(r"[-]", string)):
        data = string.split('-')
        for d in data:
            if (len(d) != 4):
                return False

        comData = ''.join(data)
        if (len(comData) != 16):
            return False
        if (re.search(r"(.)\1{3}", comData)):
            return False
    if (re.search(r"(.)\1{3}", string)):
        return False
    return True


for _ in range(int(input())):
    print("Valid" if validateCreditCard(input()) else "Invalid")
