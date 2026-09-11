class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = defaultdict(int)

        for i in range(len(nums)):
            tmp[nums[i]] = i
        
        for i in range(len(nums)):
            complment = target-nums[i]
            if complment in tmp and tmp[complment] != i:
                return[i, tmp[complment]]
        
        return []