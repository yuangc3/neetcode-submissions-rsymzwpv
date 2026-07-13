class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]* (n+1) for _ in range(m+1)]#n = 6, m = 3 
        if m == 1 and n == 1:
            return 1

        for i in range(m-1, -1, -1):#2
            for j in range(n-1, -1, -1):#5
                cache[m-1][n-1] = 1
                cache[i][j] = cache[i+1][j] + cache[i][j+1]
            print(cache)

        return cache[0][0]
        