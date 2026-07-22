class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for v in s:
            if stack:
                last = stack[-1]
                if self.is_pair(last, v):
                    stack.pop()
                    continue
            stack.append(v)
        return not stack
    
    def is_pair(self, l1, l2):
        if (l1 == "(" and l2 == ")") or (l1 == "{" and l2 == "}") or (l1 == "[" and l2 == "]"):
            return True
        return False 
        