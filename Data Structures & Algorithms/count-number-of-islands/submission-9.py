class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1],[0, 1]]
                for r, c in directions:
                    new_col = col + c
                    new_row = row + r
                    if 0 <= new_col < cols and 0<=new_row < rows and grid[new_row][new_col] == "1":
                        q.append([new_row, new_col])
                        grid[new_row][new_col] = "0"
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands