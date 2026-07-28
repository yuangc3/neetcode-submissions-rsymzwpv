class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n != 1:
            total = 0
            for num in str(n):
                total += (int(num)*int(num))
            if total in temp:
                return False
            temp.add(total)
            n = total
        return True

        
