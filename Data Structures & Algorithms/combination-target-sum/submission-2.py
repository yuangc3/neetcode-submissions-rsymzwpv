class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, temp, total):
            if total == target:
                res.append(temp.copy())
                return
            if i >= len(nums) or total > target:
                return
            temp.append(nums[i])
            backtrack(i,temp, total+nums[i])
            temp.pop()
            backtrack(i+1, temp, total)
        
        backtrack(0, [], 0)
        return res
