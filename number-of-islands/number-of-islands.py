class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != "1" or (r,c) in visit):
                return 
            visit.add((r,c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
            
            
        def bfs(r,c):
            queue = deque((r,c))
            visit = set()
            while queue:
                visit.add((r,c))
                r,c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != "1" or (row,col) in visit):
                        continue
                    queue.append((row,col))
                    
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands
        
        
        # return count
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()
#         count = 0
        
#         def dfs(r,c):
#             if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != "1" or (r,c) in visit):
#                 return 
            
#             visit.add((r,c))
#             directions = [[1,0],[0,1],[-1,0],[0,-1]]
#             for dr, dc in directions:
#                 row, col = r + dr, c + dc
#                 dfs(row, col)
            
        
#         for i in range(ROWS):
#             for j in range(COLS):
#                 if (i,j) not in visit and grid[i][j] == "1":
#                     dfs(i, j)
#                     count += 1
        
#         return count