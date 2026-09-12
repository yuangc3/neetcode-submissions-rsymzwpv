class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        count = [0] *len(nums)

        for i in range(len(nums)):
            count[i] = prefix
            prefix *= nums[i]
        #[1. 1. 2. 8]
        #[ 48   ,24 ,  6 , 1]
        for i in range(len(nums)-1, -1, -1):
            count[i] = postfix*count[i]
            postfix *= nums[i]

        return count