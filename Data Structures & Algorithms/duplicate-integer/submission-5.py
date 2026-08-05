class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = defaultdict(int)

        for n in nums:
            temp[n] += 1
        for n in nums:
            if temp[n] > 1:
                return True
        return False 