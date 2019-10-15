from itertools import groupby

string = list(input())
groups = groupby(string, key=lambda x: x[0])
for key, group in groups:
    print((len(list(group)), int(key)), end=' ')
