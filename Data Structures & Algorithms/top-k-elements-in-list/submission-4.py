class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for n in nums:
            count[n] += 1
        
        heap = []
        for values, freq in count.items():
            heapq.heappush(heap, (-freq, values))
        

        for i in range(k):
            freq, val = heapq.heappop(heap)
            res.append(val)
        return res
