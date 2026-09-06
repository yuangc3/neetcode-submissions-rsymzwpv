class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def backtrack(i, temp, cur_val):
            if cur_val == target:
                res.append(temp.copy())
                return
            if i >= len(candidates) or cur_val >target:
                return
            #want it
            temp.append(candidates[i])
            backtrack(i+1, temp, cur_val+candidates[i])

            #no
            temp.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, temp, cur_val)
        
        backtrack(0, [], 0)
        return res
                