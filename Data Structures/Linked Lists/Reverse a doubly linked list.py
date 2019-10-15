def reverse(head):
    last = None
    current = head
    while current != None:
        nextNode = current.next
        current.next = last
        current.prev = nextNode
        last = current
        current = nextNode
    return last
