class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        
        def dfs(r,c):
            res = 0
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr, dc in directions:
                res += dfs(r +dr, c + dc)
            return 1 + res
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = max(res, dfs(r,c))
                    
        return res