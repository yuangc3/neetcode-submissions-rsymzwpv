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


    def is_pair(self, last, current):
        if (last == "(" and current == ")") or (last == "[" and current == "]") or (last == "{" and current == "}"):
            return True
        return False 

