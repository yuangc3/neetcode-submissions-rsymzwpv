class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count nodes
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        res = ListNode(0, head)
        groupPrev = res
        curr = head

        # 一共有 count // k 组需要 reverse
        for _ in range(count // k):

            groupStart = curr
            prev = None

            # reverse k nodes
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # prev = 当前组新的 head
            # groupStart = 当前组新的 tail
            # curr = 下一组的 head

            groupPrev.next = prev
            groupStart.next = curr

            # 下一轮
            groupPrev = groupStart

        return res.next