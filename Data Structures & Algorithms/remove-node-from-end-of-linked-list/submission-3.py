# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        Idx = N - n

        if Idx == 0:
            return head.next
        dummy = temp = head
        for i in range(N-1):
            if (i+1) == Idx:
                temp.next = temp.next.next
                break
            temp = temp.next
        return dummy