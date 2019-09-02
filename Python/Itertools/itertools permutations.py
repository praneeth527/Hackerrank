from itertools import permutations

string = input().split()
sortedString = list(string[0])
sortedString.sort()
outList=list(permutations(sortedString,int(string[1])))
for tup in outList:
    print(''.join(tup))
