class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(nums, pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return res 
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    backtrack(nums,pick)
                    subset.pop()
                    pick[i] = False
        backtrack(nums, [False]*len(nums))
        return res