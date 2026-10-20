class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)

        for i in range(len(nums)):
            temp[nums[i]] = i
        

        for i in range(len(nums)):
            complment = target - nums[i]
            if complment in temp and temp[complment] != i:
                return [i, temp[complment]]
            
        return -1