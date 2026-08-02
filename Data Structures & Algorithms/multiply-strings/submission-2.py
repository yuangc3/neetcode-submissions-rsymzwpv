class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for l1 in range(len(num1)):
            for l2 in range(len(num2)):
                digit = int(num1[l1])*int(num2[l2])
                res[l1+l2] += digit
                res[l1+l2+1] += (res[l1+l2]//10)
                res[l1+l2] = res[l1+l2]%10
        
        res, beg = res[::-1], 0 
        while beg < len(res) and res[beg] == 0:
            beg += 1 
        res = map(str, res[beg:])
        return "".join(res)