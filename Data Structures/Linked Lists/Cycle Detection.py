def has_cycle(head):
    l = []
    while head != None:
        if head.next in l:
            return 1
        else:
            l.append(head.next)
        head = head.next
    return 0


# Alternative and efficient Floyd cycle Finding Algorithm (tortoise and hare algorithm)
def has_cycle(head):
    slow = head
    fast = head
    while slow and fast:
        fast = fast.next
        if slow == fast:
            return 1
        if fast == None:
            return 0
        fast = fast.next
        if fast == slow:
            return 1
        slow = slow.next
    return 0
