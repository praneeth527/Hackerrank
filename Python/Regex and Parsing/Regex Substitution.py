import re


def matched(string):
    d = {
        '&&': 'and',
        '||': 'or'
    }
    return d[string.group(0)]


pattern = re.compile(r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)')
for _ in range(int(input())):
    print(re.sub(pattern, matched, input()))
