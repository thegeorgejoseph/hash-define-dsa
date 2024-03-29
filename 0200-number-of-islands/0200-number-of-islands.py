class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()
        
        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != "1":
                return 
            visit.add((r,c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
        
        def bfs(r,c):
            queue = deque([(r,c)])
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] != "1":
                        continue
                    visit.add((r,c))
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        queue.append((row,col))
            
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    # dfs(r,c)
                    bfs(r,c)
                    islands += 1
        
        return islands