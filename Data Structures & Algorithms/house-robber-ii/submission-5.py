class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <2:
            return nums[0]
        def rob1(self, num):
            rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1 .. .]
            for n in num:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        new_list = nums[1:]
        new_list2 = nums.copy()
        new_list2.pop()
        temp1 = rob1(self, new_list)
        temp2 = rob1(self, new_list2)
        return max(temp1, temp2)