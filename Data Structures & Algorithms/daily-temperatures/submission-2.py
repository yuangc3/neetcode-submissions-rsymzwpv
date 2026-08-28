class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #moniic stack

        res = [0] *len(temperatures)
        stack = [] #storing [temp, idx]

        for i, t in enumerate(temperatures):

            while stack and t>stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i-stackIdx
            stack.append([t, i])
        return res

