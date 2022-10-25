class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        EMPTY = pow(2,31)-1
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        while queue:  
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or rooms[row][col] != EMPTY):
                        continue
                    rooms[row][col] = rooms[r][c] + 1
                    queue.append((row, col))
        