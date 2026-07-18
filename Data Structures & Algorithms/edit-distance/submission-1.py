class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        operation = 0
        dp = {}
        def dfs(i, j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
                #delete
            else:
                dele = dfs(i+1, j)
                #insert
                insert= dfs(i, j+1)
                res = min(dele, insert)
                #replace
                replace = dfs(i+1, j+1)
                res = min(res, replace)
                dp[(i, j)] = res +1
            return dp[(i, j)]
        return dfs(0, 0)
