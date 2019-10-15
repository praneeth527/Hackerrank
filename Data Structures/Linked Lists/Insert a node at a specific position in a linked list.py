def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        return new_node
    count = 0
    current = head
    previous = head
    while current.next != None and count < position:
        count += 1
        if count == position:
            new_node.next = current.next
            current.next = new_node

            return head
        previous = current
        current = current.next
