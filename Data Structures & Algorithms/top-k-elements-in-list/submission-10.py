class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        res = []
        for n in nums:
            temp[n]+=1
        

        heap = []
        for v, c in temp.items():
            heapq.heappush(heap,(-c, v))
        


        for _ in range(k):
            c, v = heapq.heappop(heap)
            res.append(v)
        return res
