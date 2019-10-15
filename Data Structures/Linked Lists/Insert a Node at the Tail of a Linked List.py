def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    if head == None:
        head = new_node
        return head
    else:
        current = head
        while current.next != None:
            current = current.next
        current.next = new_node
        return head
