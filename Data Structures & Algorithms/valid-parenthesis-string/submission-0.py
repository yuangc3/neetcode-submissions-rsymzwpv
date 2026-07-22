class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []#( index
        star = [] #* index

        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
        while left and star:
                #( left over
            if left.pop() > star.pop():
                return False
        return not left 