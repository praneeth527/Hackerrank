def reversePrint(head):
    if head == None:
        return
    reversePrint(head.next)
    print(head.data)
