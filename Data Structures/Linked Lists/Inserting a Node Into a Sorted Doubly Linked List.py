def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    current = head
    previous = DoublyLinkedListNode(None)
    while current != None:
        if data < current.data:
            previous.next = new_node
            new_node.next = current
            new_node.prev = previous
            current.prev = new_node
            if current == head:
                return new_node
            return head
        previous = current
        current = current.next
    previous.next = new_node
    new_node.prev = previous
    return head
