class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # 1) Set classic BFS variables:
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = collections.deque()
        EMPTY = 2147483647
        GATE = 0

        # 2) Enqueue all the Gates first since
        # Search from the gates to the empty rooms:
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        # 3) Peform BFS loop:
        # initiate BFS from all gates at the same time:
        while queue:
            # a) Get gateway:
            curR, curC = queue.popleft()

            # b) Record distance from neighbors to Gates:
            for rd, cd in directions:
                r = rd + curR
                c = cd + curC

                # c) Skip walls and check boundaries:
                if r not in range(ROWS) or c not in range(COLS) or rooms[r][c] != EMPTY:
                    continue

                # Record actual distance on each cell:    
                rooms[r][c] = rooms[curR][curC] + 1
                queue.append((r, c))