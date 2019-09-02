from collections import Counter, OrderedDict
from itertools import islice
string = input()

counter = Counter(string)
c = (sorted(Counter(counter).items(), key=lambda x: x[0]))
out=(sorted(c, key=lambda x: x[1], reverse=True))
for data in islice(out,3):
    print(data[0],data[1])
