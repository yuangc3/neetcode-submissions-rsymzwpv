class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 1
        dp = {}

        def dfs(i, j):
            if i == len(s) and j < len(t):
                return 0
            if j == len(t):
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            #skip it
            res = dfs(i+1, j)
            
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            dp[(i, j)] = res 
            return res 
        return dfs(0, 0)
            #do not take it 