class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        colSet = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy[:])
                return
            
            for c in range(n):
                if c in colSet or r + c in posDiag or r - c in negDiag:
                    continue
                
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
                
        
        backtrack(0)
        return res
                