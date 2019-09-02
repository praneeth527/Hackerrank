from collections import deque

n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    if command[0] == 'pop':
        d.pop()
    if command[0] == 'popleft':
        d.popleft()
    if command[0] == 'appendleft':
        d.appendleft(int(command[1]))
print(*d)
