class Solution:
    def isHappy(self, n: int) -> bool:
        char = set()

        while n != 1:
            if n in char:
                return False
            char.add(n)
            s = str(n)
            total = 0
            for v in s:
                total += int(v)*int(v)
            n = total
        return True 

        