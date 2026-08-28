class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        leftmost = [-1]*len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)
        
        stack =[]
        rightmost = [len(heights)]*len(heights)
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)
        
        max_area = 0 
        for i in range(len(heights)):
            width = rightmost[i] - leftmost[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area

        
