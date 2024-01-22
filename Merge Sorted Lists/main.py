class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

#using dummy
def mergeTwoLists(list1:ListNode,list2:ListNode) -> ListNode:
    """
    Gets 2 sorted linked lists, returns a merged list with the values ordered in ascending order.
    If list not initialized returns empty None
    """
    dummy = ListNode()
    cur = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            val = list1.val
            list1 = list1.next
        else:
            val = list2.val
            list2 = list2.next
        cur.next = ListNode(val)
        cur = cur.next
        
    
    if list1 or list2:
        cur.next = list1 if not list2 else list2
    
    return dummy.next #first element is a 0, so returns the next that is the appendend list


l1 = ListNode(1,ListNode(2,ListNode(4)))
l2 = ListNode(1,ListNode(3,ListNode(4)))

a = mergeTwoLists(l1,l2)


while a:
    print(a.val)
    a = a.next