class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def backtrack(openN, endN):
            if openN == endN == n:
                res.append("".join(stack))
                return
            
            #"(" not enough
            if openN < n:
                stack.append('(')
                backtrack(openN+1, endN)
                stack.pop()
            if openN > endN:
                stack.append(")")
                backtrack(openN, endN+1)
                stack.pop()
        backtrack(0, 0)
        return res
