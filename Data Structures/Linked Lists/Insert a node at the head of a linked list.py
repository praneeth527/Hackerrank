def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if llist == None:
        return new_node
    else:
        new_node.next = llist
        return new_node
