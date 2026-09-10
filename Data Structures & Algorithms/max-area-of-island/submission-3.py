class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        max_area = 0 

        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            queue = deque([(r, c)])
            grid[r][c] = 0
            area = 1
            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for r, c in directions:
                    new_row = r + row
                    new_col = c + col
                    if 0 <= new_row <= rows-1 and 0 <= new_col <= cols-1 and grid[new_row][new_col] == 1:
                        area += 1
                        queue.append((new_row, new_col))     
                        grid[new_row][new_col] = 0
            return area 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        return max_area



