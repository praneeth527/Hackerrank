def merge_the_tools(string, k):
    li = []
    # your code goes here
    n = len(string)
    j = 0
    l = 0
    for i in range(n):
        l = l + k
        s = (string[j:l])
        if (s != ''):
            for i in range(len(s)):
                if (s[i] not in li):
                    li.append(s[i])
            o = ''.join(li)
            print(o)
            li.clear()

        j = j + k
