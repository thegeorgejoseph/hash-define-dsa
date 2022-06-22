class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r,c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft() #change this to pop for DFS
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] != "0" and (r,c) not in visit):
                        visit.add((r,c))
                        queue.append((r,c))
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
            