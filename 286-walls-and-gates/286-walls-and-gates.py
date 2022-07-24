class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        EMPTY = 2147483647
        queue = deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or rooms[row][col] != EMPTY):
                        continue
                    # because you are only moving one step at a time so if another gate finds an already updated cell, no need to replace it because the closest distance has already been recorded
                    rooms[row][col] = 1 + rooms[r][c]
                    queue.append((row,col))
                