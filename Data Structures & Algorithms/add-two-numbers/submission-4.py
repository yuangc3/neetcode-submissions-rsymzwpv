# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = temp = ListNode()
        while l1 or l2 or carry:
            va1 = l1.val if l1 else 0
            va2 = l2.val if l2 else 0
            v = va1 + va2+carry
            carry = v // 10
            val = v % 10

            new = ListNode(val)
            temp.next = new
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next