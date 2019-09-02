def swap_case(s):
    li = list(s)
    for i in range(len(li)):
        if (li[i].isalpha()):
            if (li[i].islower()):
                li[i] = li[i].upper()
            else:
                li[i] = li[i].lower()
    data = ''.join(li)
    return data
