class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp =defaultdict(int)
        res = []
        for n in nums:
            temp[n]+=1
        heap = []

        for key, freq in temp.items():
            heapq.heappush(heap, (-freq, key))
        

        for i in range(k):
            val, freq = heapq.heappop(heap)
            res.append(freq)
        return res