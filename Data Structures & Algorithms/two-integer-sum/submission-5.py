class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)

        for i in range(len(nums)):
            temp[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp and i != temp[complement]:
                return[i, temp[complement]]
            
