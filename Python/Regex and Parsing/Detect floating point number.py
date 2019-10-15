import re

compiled_pattern = re.compile(r"^[+-]?[0-9]*\.[0-9]+$")
for _ in range(int(input())):
    if (re.match(compiled_pattern, input())):
        print(True)
    else:
        print(False)
