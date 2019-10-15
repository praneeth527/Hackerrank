N, X = list(map(int, input().split()))
lists = []
for _ in range(X):
    lists.append(list(map(float, input().split())))
outList = zip(*lists)
for tup in outList:
    print(sum(tup) / len(tup))
