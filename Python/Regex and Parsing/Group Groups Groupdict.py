import re

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# \1 is a backreference. It matches, what ever matched in your brackets
if (m):
    print(m.group(1))
else:
    print(-1)
