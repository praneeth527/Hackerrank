def findSequence(x, lastAnswer, n):
    return (x ^ lastAnswer) % n


def type1(seq, y):
    global seqList
    seqList[seq].append(y)


def type2(seq, y):
    global seqList
    return seqList[seq][y % len(seqList[seq])]


def dynamicArray(n, queries):
    # Write your code here
    global seqList
    seqList = []
    lastAnswer = 0
    result = []
    for _ in range(n):
        seqList.append([])
    for i in range(len(queries)):
        if (queries[i][0] == 1):
            type1(findSequence(queries[i][1], lastAnswer, n), queries[i][2])
        if (queries[i][0] == 2):
            lastAnswer = (type2(findSequence(queries[i][1], lastAnswer, n), queries[i][2]))
            result.append(lastAnswer)
    return result
