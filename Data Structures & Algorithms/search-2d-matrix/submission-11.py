class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix)-1
        rows, cols = len(matrix), len(matrix[0])

        while top <= down:
            mid = (top + down) // 2
            #value is at the mid row

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l, r = 0, cols-1
                while l <= r:
                    middle = (l+r) // 2
                    if target == matrix[mid][middle]:
                        return True
                    elif target < matrix[mid][middle]:
                        r = middle-1
                    else:
                        l = middle +1
                return False 
            elif matrix[mid][0]>target:
                down = mid -1
            
            elif matrix[mid][-1] < target:
                top = mid + 1
        return False
            
