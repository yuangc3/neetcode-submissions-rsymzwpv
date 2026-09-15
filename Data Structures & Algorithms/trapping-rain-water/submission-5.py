class Solution:
    def trap(self, height: List[int]) -> int:
        countl = [0] *len(height)

        countr = [0]*len(height)

        countl[0] = height[0]

        for i in range(1, len(height)):
            countl[i] = max(countl[i-1], height[i])
        

        countr[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            countr[i] = max(countr[i+1], height[i])

        
        res = 0 
        for i in range(len(height)):
            res += min(countl[i], countr[i])-height[i]
        
        return res