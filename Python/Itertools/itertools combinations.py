from itertools import combinations

string = input().split()
sortedString = list(string[0])
sortedString.sort()
k = int(string[1])
outList = []
for i in range(1,k+1):
    outList.append(list(combinations(sortedString, i)))
for l in outList:
    for out in l:
        print(''.join(out))
