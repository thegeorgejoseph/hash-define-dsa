class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return 
            
            board[r][c] = "T"
            dfs(r, c +1)
            dfs(r, c - 1)
            dfs(r + 1,c)
            dfs(r - 1,c)
            
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0,ROWS-1] or c in [0,COLS-1]:
                    if board[r][c] == "O":
                        dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
    