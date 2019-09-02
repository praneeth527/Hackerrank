def print_formatted(number):
    l = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i, l))
