def count_substring(string, sub_string):
    h = len(string)
    n = len(sub_string)
    li = []
    for i in range(h):
        if (i + n <= h):
            li.append(string[i:i + n])
        else:
            break
    cou = li.count(sub_string)

    return cou
