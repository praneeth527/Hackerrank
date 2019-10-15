def getNode(head, positionFromTail):
    if positionFromTail < 0:
        return None
    temp = head
    count = 0
    while count < positionFromTail and temp != None:
        temp = temp.next
        count += 1
    if temp == None or count < positionFromTail:
        return None
    n = head
    while temp.next != None:
        temp = temp.next
        n = n.next
    return n.data
