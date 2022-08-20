class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        queue = deque([])
        
        def bfs():
            while queue:
                r,c = queue.popleft()
                if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != "1"):
                    continue
                visit.add((r,c))
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    queue.append([row,col])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    queue.append([r,c])
                    bfs()
                    count += 1
        
        return count
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