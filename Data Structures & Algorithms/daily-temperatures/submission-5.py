class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []#temp, idx 

        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, i = stack.pop()
                res[i] = idx-i
            stack.append((t, idx))

        return res  

