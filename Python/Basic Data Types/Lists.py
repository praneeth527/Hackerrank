li = []
n = int(input())
for i in range(n):
    q = input()
    query = q.split()
    if (query[0] == 'insert'):
        li.insert(int(query[1]), int(query[2]))
    elif (query[0] == 'remove'):
        li.remove(int(query[1]))
    elif (query[0] == 'append'):
        li.append(int(query[1]))
    elif (query[0] == 'pop'):
        li.pop()
    elif (query[0] == 'print'):
        print(li)
    elif (query[0] == 'sort'):
        li.sort()
    elif (query[0] == 'reverse'):
        li.reverse()
