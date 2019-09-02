n = int(input())
q = (input())
data = q.split()
for i in range(len(data)):
    data[i] = int(data[i])

t = tuple(data)

print(hash(t))
