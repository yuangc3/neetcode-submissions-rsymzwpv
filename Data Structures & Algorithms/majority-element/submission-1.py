class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        z = len(nums)

        temp = defaultdict(int)
        for n in nums:
            temp[n] += 1

        for key, count in temp.items():
            if count > z/2:
                return key
        return -1