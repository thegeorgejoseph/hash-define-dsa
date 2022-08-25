class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def bfs(r,c):
            queue = deque([(r,c)])
            while queue:
                r,c = queue.popleft()
                if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != "1" or (r,c) in visit):
                    continue
                visit.add((r,c))
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    queue.append((row,col))
    
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
#         ROWS, COLS = len(grid), len(grid[0])
#         islands = 0
#         visit = set()
#         directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
#         def dfs(r,c):
#             if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != "1" or (r,c) in visit):
#                 return 
#             visit.add((r,c))
#             for dr, dc in directions:
#                 row, col = r + dr, c + dc
#                 dfs(row, col)
                    
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if (r,c) not in visit and grid[r][c] == "1":
#                     islands += 1
#                     dfs(r,c)
#         return islands
        
        
        