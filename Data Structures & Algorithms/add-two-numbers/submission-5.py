# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = curr = ListNode()
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0 
            if l2:
                val2 = l2.val
            else:
                val2 = 0 
            val = val1 + val2 + carry
            carry = val // 10
            new = val % 10
            temp = ListNode(new)
            curr.next = temp
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next 
