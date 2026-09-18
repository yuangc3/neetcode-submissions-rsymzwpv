class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        up, bottom = 0, rows-1

        while up <= bottom:
            mid = (up+bottom)//2 
            if matrix[mid][-1] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid -1
            else:
                l, r = 0, cols-1
                while l <=r:
                    m = (l+r)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m+1
                    else:
                        r = m -1
                return False
        return False
                 