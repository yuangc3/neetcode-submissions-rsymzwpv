class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = defaultdict(int)

        for n in nums:
            temp[n] +=1
        
        for value, count in temp.items():
            if count >1:
                return value
        return -1

        