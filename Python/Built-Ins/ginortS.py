string = input()
l, u, o, e = [], [], [], []
for letter in string:
    if (letter.islower()):
        l.append(letter)
    elif (letter.isupper()):
        u.append(letter)
    elif (letter.isdigit()):
        if (int(letter) % 2 == 0):
            e.append(int(letter))
        else:
            o.append(int(letter))
l.sort()
u.sort()
o.sort()
e.sort()
out = l + u + [str(i) for i in o] + [str(i) for i in e]
print(''.join(out))
