class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()
        
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != 1):
                return 0
            visit.add((r,c))
            res = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res += dfs(row, col)
            return res
            
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        
        return res