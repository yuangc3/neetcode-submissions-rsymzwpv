class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def backtrack(i, openN, endN):
            if openN == endN == n:
                res.append("".join(subset))
            
            if openN < n:
                subset.append("(")
                backtrack(i+1, openN+1, endN)
                subset.pop()
            
            if endN < openN:
                subset.append(")")
                backtrack(i+1, openN, endN+1)
                subset.pop()
        
        backtrack(0, 0, 0)
        return res

