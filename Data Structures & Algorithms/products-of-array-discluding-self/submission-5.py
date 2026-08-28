class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        postfix = 1 
        res = [1]*len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix*res[i]
            postfix *= nums[i]
        

        return res 