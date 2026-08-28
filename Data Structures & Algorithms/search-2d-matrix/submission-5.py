class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        up, bottom = 0, rows-1
        while up <= bottom:
            mid = (up+bottom) // 2
            if matrix[mid][-1] < target:
                up = mid + 1 
            elif matrix[mid][0] > target:
                bottom = mid - 1 
            else:
                left, right = 0, cols-1
                while left <= right:
                    middle = (left +right) // 2
                    if matrix[mid][middle] > target:
                        right = middle-1
                    elif matrix[mid][middle] < target:
                        left = middle+1
                    else:
                        return True
                return False
        return False 
            