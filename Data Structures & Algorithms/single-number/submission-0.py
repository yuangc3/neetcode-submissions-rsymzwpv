class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = defaultdict(int)
        res = 0
        for n in nums:
            temp[n] += 1
        
        for n in temp:
            if temp[n] == 1:
                return n

        
        
