class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh, time = 0, 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1):
                        continue
                    fresh -= 1
                    grid[row][col] = 2
                    queue.append((row, col))
            time += 1
        return time if fresh == 0 else -1