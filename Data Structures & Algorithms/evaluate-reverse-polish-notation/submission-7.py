class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0 
        for n in tokens:
            if n == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            
            elif n == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)       
            elif n == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)  
            elif n == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:  
                stack.append(int(n))
        return stack[0] 

                