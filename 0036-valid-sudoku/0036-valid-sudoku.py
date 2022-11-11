class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows, cols, sub = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub[(r//3, c//3)]: 
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub[(r//3, c//3)].add(board[r][c])
        return True