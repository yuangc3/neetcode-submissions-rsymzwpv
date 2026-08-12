class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_most = [0] *n
        right_most = [0]*n

        left_most[0] = height[0]
        for i in range(1, n):
            left_most[i] = max(left_most[i-1], height[i])
        

        right_most[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            right_most[i] = max(right_most[i+1], height[i])
        

        res = 0
        for i in range(n):
            res += min(left_most[i], right_most[i]) - height[i]
        
        return res 