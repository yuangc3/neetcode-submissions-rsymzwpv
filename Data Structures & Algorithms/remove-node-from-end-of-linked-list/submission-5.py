# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        idx = 0 

        curr = head
        while curr:
            idx+=1
            curr = curr.next
        
        dummy = res = head
        idex = idx - n

        if idex == 0:
            return res.next
        for i in range(idex):
            if i+1 == idex:
                dummy.next =dummy.next.next
                break
            dummy = dummy.next
        
        return res
