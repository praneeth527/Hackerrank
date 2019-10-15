def removeDuplicates(head):
    temp = SinglyLinkedListNode(None)
    original = temp
    l = []
    while head != None:
        if head.data not in l:
            l.append(head.data)
            original.next = head
            original = original.next
        else:
            original.next = None
        head = head.next
    return temp.next
