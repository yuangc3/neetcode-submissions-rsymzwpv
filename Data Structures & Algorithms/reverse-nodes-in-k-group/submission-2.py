# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0 

        curr = head
        while curr:
            count+=1
            curr = curr.next
        res = ListNode()
        groupPrev = res
        curr = head
        for _ in range(count//k):
            prev = None
            groupStart = curr

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            groupPrev.next = prev
            groupStart.next = curr

            groupPrev = groupStart
        
        return res.next
            
