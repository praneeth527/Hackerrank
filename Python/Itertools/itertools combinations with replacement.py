from itertools import combinations_with_replacement

string = input().split()
sortedString = list(string[0])
sortedString.sort()
k = int(string[1])

outList = (list(combinations_with_replacement(sortedString, k)))
for l in outList:
    print(''.join(l))
