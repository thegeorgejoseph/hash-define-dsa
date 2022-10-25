class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return 
            board[r][c] = "T"
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS-1] or c in [0, COLS-1]) and board[r][c] == "O":
                    dfs(r,c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        