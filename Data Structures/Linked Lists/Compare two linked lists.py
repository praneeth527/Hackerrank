def compare_lists(llist1, llist2):
    while llist1 != None and llist2 != None:
        if llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0

    if llist1 == None and llist2 == None:
        return 1
    return 0
