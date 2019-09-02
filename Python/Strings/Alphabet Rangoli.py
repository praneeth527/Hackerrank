def printRow(n, i):
    ulPart = []
    row = '-' * (2 * n - 2 - (i * 2))
    for d in range(1, i + 1):
        row = row + chr((n - d) + ord('a')) + '-'
    line = row + chr(n - i - 1 + ord('a'))
    line = line + row[::-1]
    return line


def print_rangoli(size):
    rows = []
    for i in range(size):
        rows.append(printRow(size, i))
    totalLines = rows + rows[::-1]
    del totalLines[size]
    for row in totalLines:
        print(row)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
