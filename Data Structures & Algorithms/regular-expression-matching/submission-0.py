import string
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        temp = set(string.ascii_lowercase)
        dp = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[(i, j)]
            match = False
            if i < len(s):
                if s[i] == p[j] or p[j] ==".":
                    match = True

            if j+1 < len(p) and p[j+1] == "*":
                use = False
                if match:
                    use = dfs(i+1, j)
                skip = dfs(i, j+2)
                dp[(i, j)] = skip or use

            else:
                if match:
                    dp[(i, j)] = dfs(i + 1, j + 1)
                else:
                    dp[(i, j)] = False

            return dp[(i, j)]
        return dfs(0, 0)
