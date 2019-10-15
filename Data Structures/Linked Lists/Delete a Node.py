def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    count = 1
    current = head
    previous = head
    while current.next != None:

        if count == position + 1:
            previous.next = current.next
            return head
        previous = current
        current = current.next
        count += 1
