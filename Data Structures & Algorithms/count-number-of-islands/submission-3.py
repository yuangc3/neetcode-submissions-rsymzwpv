class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0,-1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] ="0"
            while queue:
                row, col = queue.popleft()
                for r, c in directions:
                    new_row = row + r 
                    new_col = col + c
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                        queue.append([new_row, new_col])
                        grid[new_row][new_col] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r, c)
                    island += 1
        return island
            
            