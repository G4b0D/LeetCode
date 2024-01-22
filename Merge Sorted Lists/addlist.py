class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next



#without dummy
def add(l1:ListNode):
    if not l1:
        return None
    newHead = ListNode(l1.val*2)
    cur = newHead
    l1 = l1.next

    while l1:
        cur.next = ListNode(l1.val *2)
        cur = cur.next
        l1 = l1.next
    
    return newHead

#with dummy (cleaner solution)
def add2(l1: ListNode):
    dummy = ListNode()
    cur = dummy

    while l1:
        cur.next = ListNode(l1.val)
        cur = cur.next
        l1 = l1.next