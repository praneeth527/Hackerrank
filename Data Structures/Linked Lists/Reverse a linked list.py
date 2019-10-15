def reverse(head):
    prev = None
    current = head
    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
