class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        mid = sum(nums) // 2
        total = 0 
        def backtrack(i, curr):
            if curr == mid:
                return True
            if i == len(nums) or curr > mid:
                return False
        
            if backtrack(i+1, curr+nums[i]):
                return True
            if backtrack(i+1, curr):
                return True
            return False
        
        return backtrack(0, 0)


