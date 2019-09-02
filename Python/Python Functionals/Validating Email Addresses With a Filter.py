def fun(s):
    part1 = s.split('@', 1)
    if (len(part1) < 2):
        return False
    userName = part1[0]
    if (len(userName) < 1):
        return False
    remPart = part1[1].split('.', 1)
    if (len(remPart) < 2):
        return False
    websiteName, extensionName = remPart[0], remPart[1]
    for letter in userName:
        if ((not letter.isalnum()) and letter != '_' and letter != '-'):
            return False
    for letter in websiteName:
        if not letter.isalnum():
            return False
    if (len(websiteName) < 1):
        return False
    if (len(extensionName) > 3 or (not extensionName.isalpha()) or len(extensionName) == 0):
        return False
    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
