import re

string = input()
pattern = input()
index = 0

if re.search(pattern, string):
    while index + len(pattern) < len(string):
        r = re.search(pattern, string[index:])
        if r:
            print((index + r.start(), index + r.end() - 1))
            index += r.start() + 1
        else:
            break
else:
    print((-1, -1))