class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        

        rows = len(img)
        cols = len(img[0])
        if rows == 1 and cols == 1:
            return img
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0 

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = dr + r, dc + c
                        if 0<=nr <rows and 0 <= nc < cols:
                            total += img[nr][nc]
                            count += 1

                res[r][c] = total // count
        return res           

