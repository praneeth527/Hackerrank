def printLinkedList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next
