def mergeLists(head1, head2):
    mergenode = SinglyLinkedListNode(None)
    head = mergenode
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            mergenode.next = head1
            head1 = head1.next
        else:
            mergenode.next = head2
            head2 = head2.next
        mergenode = mergenode.next
    if head1 == None:
        mergenode.next = head2
    else:
        mergenode.next = head1
    return head.next
