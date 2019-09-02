import re

c = "qwrtypsdfghjklzxcvbnm"
compiled_pattern = re.compile(r"(?<=[" + c + "])[aeiou]{2,}(?=[" + c + "])", re.IGNORECASE)  # positive lookbehind ?<=
res = (re.findall(compiled_pattern, input()))
if (len(res) > 0):
    print('\n'.join(res))
else:
    print(-1)
