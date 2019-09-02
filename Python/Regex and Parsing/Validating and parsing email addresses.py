import email.utils
import re

compiled_pattern = re.compile(r"^[a-zA-Z]{1}[a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
for _ in range(int(input())):
    inputString = input()
    (name, e) = email.utils.parseaddr(inputString)
    if re.match(compiled_pattern, e):
        print(inputString)
