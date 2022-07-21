class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r,c):
            queue = deque([(r,c)])
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while queue:
                ir, ic = queue.popleft() #changing this to pop will result in DFS
                for dr, dc in directions:
                    xr, xc = ir + dr, ic + dc
                    if (xr < 0 or xc < 0 or xr >= ROWS or xc >= COLS or (xr,xc) in visit or grid[xr][xc] == "0"):
                        continue
                    visit.add((xr,xc))
                    queue.append((xr,xc))
            
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        return res
        
        
        
        
        
        
#         if not grid:
#             return 0
        
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()
#         res = 0
#         def dfs(r,c):
#             if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0"):
#                 return
            
#             visit.add((r,c))
#             directions = [[0,1],[1,0],[-1,0],[0,-1]]
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)
            
    
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1" and (r,c) not in visit:
#                     res += 1
#                     dfs(r,c)
#         return res
        
        
        
        
        
        
#         if not grid:
#             return 0
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()
#         islands = 0
        
#         def bfs(r,c):
#             queue = collections.deque()
#             visit.add((r,c))
#             queue.append((r,c))
#             while queue:
#                 row, col = queue.popleft() #change this to pop for DFS
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]
#                 for dr, dc in directions:
#                     r,c = row + dr, col + dc
#                     if (r in range(ROWS) and c in range(COLS) and grid[r][c] != "0" and (r,c) not in visit):
#                         visit.add((r,c))
#                         queue.append((r,c))
        
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1" and (r,c) not in visit:
#                     bfs(r,c)
#                     islands += 1
#         return islands
            