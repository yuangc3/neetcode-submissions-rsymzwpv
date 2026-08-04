class Solution:
    def countBits(self, n: int) -> List[int]:

        def count_1(num):
            res = 0

            while num>0:
                num = num &(num-1)
                res += 1 
            return res 
        res = []
        for i in range(n+1):
            res.append(count_1(i))
        return res 