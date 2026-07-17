class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(r, c, preVal):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] <= preVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            res = max(res, 1+ dfs(r+1, c, matrix[r][c]))
            res = max(res, 1+ dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+ dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+ dfs(r, c-1, matrix[r][c]))
            dp[(r, c)] = res
            return res 
        
        LIP = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        return max(dp.values())



