class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        res = []
        for n in nums:
            temp[n] += 1

        
        heap = []
        for value, freq in temp.items():
            heapq.heappush(heap, (-freq, value))
    
        for i in range(k):
            freq, value = heapq.heappop(heap)
            res.append(value)
        
        return res
