class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacv, atlv = set(), set()
        
        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, visit, heights[r][c])
            
        
        for c in range(COLS):
            dfs(0,c,pacv,heights[0][c])
            dfs(ROWS-1,c,atlv,heights[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r,0,pacv,heights[r][0])
            dfs(r,COLS-1,atlv,heights[r][COLS-1])
            
        res = []
        for r,c in pacv:
            if (r,c) in atlv:
                res.append([r,c])
        return res