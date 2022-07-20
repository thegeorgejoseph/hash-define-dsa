class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != word[i]):
                return False
            visit.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                if backtrack(r + dr, c + dc,i+1): return True
            visit.remove((r,c))
            return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False