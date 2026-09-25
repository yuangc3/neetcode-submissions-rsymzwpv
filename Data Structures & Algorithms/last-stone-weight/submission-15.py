class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap= []
        if len(stones) == 1:
            return stones[0]
        for n in stones:
            heapq.heappush(heap, -n)


        while len(heap) > 1:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            if val1 == val2:
                continue
            else:
                new = abs(val1-val2)
                heapq.heappush(heap, -new)
        if len(heap) == 1:
            res = heapq.heappop(heap)
            return -res
        return 0