import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

i = 0
string = ''
while (i < m):
    for row in matrix:
        string += row[i]
    i += 1
print(re.sub(r"(?<=[a-zA-Z])[!@#$%&\s]+(?=[a-zA-Z])", ' ', string))
