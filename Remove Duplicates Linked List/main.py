class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def RemoveDuplicates(l: ListNode) -> ListNode:
    if not l:
        return l
    uniqueVals = set()
    dummy = ListNode()
    cur = dummy
    while l:
        if l.val not in uniqueVals:
            cur.next = ListNode(l.val)
            uniqueVals.add(l.val)
            cur = cur.next
        l = l.next
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next=ListNode(1)
a = RemoveDuplicates(l1)
nums = []
while a:
    nums.append(a.val)
    a = a.next
print(nums)