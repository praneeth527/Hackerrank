# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    for q in queries:
        result.append(strings.count(q))
    return result
