def findMergeNode(head1, head2):
    c1, c2 = head1, head2
    c1l, c2l = 0, 0
    while c1 != None:
        c1 = c1.next
        c1l += 1
    while c2 != None:
        c2 = c2.next
        c2l += 1
    d = abs(c1l - c2l)
    c1, c2 = head1, head2
    if c1l > c2l:
        for _ in range(d):
            c1 = c1.next
    else:
        for _ in range(d):
            c2 = c2.next
    while c1 != c2:
        c1 = c1.next
        c2 = c2.next
    return c1.data
