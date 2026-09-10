class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(i, openN, endN):
            if openN == endN == n:
                res.append("".join(subset))
                return
            if openN < n:
                subset.append("(")
                dfs(i+1, openN+1, endN)
                subset.pop()
            if endN < openN:
                subset.append(")")
                dfs(i+1, openN, endN+1)
                subset.pop()
            
        dfs(0, 0, 0)
        return res 
