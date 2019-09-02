import re

patter = r"^[789]{1}[0-9]{9}$"
for _ in range(int(input())):
    if (re.match(patter, input().strip())):
        print("YES")
    else:
        print("NO")
