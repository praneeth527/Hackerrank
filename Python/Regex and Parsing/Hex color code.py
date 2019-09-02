import re

for _ in range(int(input())):
    string = input().strip()
    r = re.findall(r'(?!^)#([a-f0-9]{6}|[a-f0-9]{3})[^\n]', string, flags=re.IGNORECASE)
    for i in r:
        print('#' + i)
