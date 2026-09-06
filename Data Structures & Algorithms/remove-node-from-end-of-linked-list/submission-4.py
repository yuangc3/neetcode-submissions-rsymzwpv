# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        idex = 0 
        curr = head
        while curr:
            idex += 1
            curr = curr.next
        
        idx = idex - n
        if idx == 0:
            return head.next
        temp = dummy = head
        for i in range(idx):
            if i+1 == idx:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
        return temp 

