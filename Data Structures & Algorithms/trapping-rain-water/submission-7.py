class Solution:
    def trap(self, height: List[int]) -> int:
        count1 = [0]* len(height)
        count2 = [0] * len(height)

        count1[0] = height[0]

        for i in range(1, len(height)):
            count1[i] = max(count1[i-1], height[i])
        

        count2[len(height)-1] = height[len(height)-1]

        for i in range(len(height)-2, -1, -1):
            count2[i] = max(count2[i+1], height[i])

        res = 0 

        for i in range(len(height)):
            res += min(count1[i], count2[i])-height[i]

        return res