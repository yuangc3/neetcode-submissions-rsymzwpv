class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0 
        heap = []
        new = 0
        if len(stones) == 1:
            return stones[0]

        for s in stones:
            heapq.heappush(heap, -s)
        print(heap)
        while len(heap) > 1:
            val = -heapq.heappop(heap)
            val2= -heapq.heappop(heap)
            if val != val2:
                new = val - val2
                heapq.heappush(heap, -new)
        if heap:
            return -heap[0]
        return 0