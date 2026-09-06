class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, temp, cur_val):
            if cur_val == target:
                res.append(temp.copy())
                return
            if i >= len(nums) or cur_val >target:
                return

            temp.append(nums[i])
            backtrack(i, temp, cur_val+nums[i])
            temp.pop()
            backtrack(i+1, temp, cur_val)
        
        backtrack(0, [], 0)
        return res
            
            

            