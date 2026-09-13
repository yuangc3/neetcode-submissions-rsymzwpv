class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        temp = set(nums)
        count = 0 

        for i in range(len(nums)):
            if (nums[i]-1) not in temp:
                length = 1
                while nums[i]+length in temp:
                    length += 1  
                count = max(count, length)
        return count
