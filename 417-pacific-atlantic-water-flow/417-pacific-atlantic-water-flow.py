class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []
        def dfs(r,c, visit, previousHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or previousHeight > heights[r][c]):
                return
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
            
        
        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
            # the starting position of DFS is usually the left most element
        
        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS-1, atlantic, heights[r][COLS-1])
        
        for r,c in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        
        return res