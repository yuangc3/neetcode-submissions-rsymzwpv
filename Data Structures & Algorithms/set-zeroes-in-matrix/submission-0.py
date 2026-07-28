class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        row, col = [False]*rows, [False]*cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True
        

        for r in range(rows):
            for c in range(cols):
                if row[r] or col[c]:
                    matrix[r][c] = 0
        