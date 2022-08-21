class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res= []
        def dfs(r,c,previousHeight, visit):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or previousHeight > heights[r][c]):
                return 
            
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, heights[r][c], visit)
        
            return            
        
        for c in range(COLS):
            dfs(0,c,heights[0][c],pac)
            dfs(ROWS-1,c,heights[ROWS-1][c],atl)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)
        
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        
        return res