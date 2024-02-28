"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printlist(self):
        nums = []
        itr = self
        while itr:
            nums.append(self.val)
            itr = itr.next
        print(nums)

def Sum2Lists(l1: ListNode,l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 and l2:
        sum = l1.val + l2.val + carry
        cur.next = ListNode(sum%10) # 9 mod 10 = 9, 11 mod 10 = 1
        carry = sum // 10  # 9 // 10 = 0, 11 // 10 = 1
        l1,l2 = l1.next, l2.next
        cur = cur.next
    while carry:
        val = 0 
        if l1:
            val = l1.val
            l1 = l1.next
        elif l2:
            val = l2.val
            l2 = l2.next
        cur.next = ListNode((val+carry)%10)
        carry = (val+carry) //10 
        cur = cur.next
    if l1 or l2:
        cur.next = l1 if l1 else l2
    return dummy.next

l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))
l2 = ListNode(9,ListNode(9,ListNode(9)))
#l2 = ListNode(1,ListNode(9))
a = Sum2Lists(l1,l2)
vals = []
while a:
    vals.append(a.val)
    a = a.next
print(vals)