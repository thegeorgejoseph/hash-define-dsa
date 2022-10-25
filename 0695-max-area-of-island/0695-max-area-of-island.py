class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()
        maxArea = 0
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != 1):
                return 0
            visit.add((r,c))
            res = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res += dfs(row, col)
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea