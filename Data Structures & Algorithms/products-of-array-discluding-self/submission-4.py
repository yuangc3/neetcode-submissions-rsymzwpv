class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix
        #[1, 2, 4,6]
        #res: [1, 1, 2, 8]
        #postfix: [48, 24, 6, 1]
        prefix = 1
        postfix = 1

        res = [1] *len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        

        for i in range(len(nums)-1, -1, -1):
            

            res[i] = postfix*res[i]
            postfix *= nums[i]
        
        return res 
