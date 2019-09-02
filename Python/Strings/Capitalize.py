# Complete the solve function below.
import re


def solve(s):
    sL = []
    for i in range(len(s)):
        sL.append(s[i])
    # print(sL)
    li = (re.findall("\s[a-z0-9A-Z]", s))
    # print(li)
    for i in range(len(li)):
        n = (s.find(li[i], i)) + 1
        sL[n] = sL[n].upper()
    # print(sL)
    sL[0] = sL[0].upper()
    out = ''.join(sL)
    return out
