class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        colSet = set()
        posDiag = set() # (r+c) pattern
        negDiag = set() # (r-c) pattern
        
        def backtrack(r):
            if r == n :
                temp = ["".join(row) for row in board]
                res.append(temp[:])
            
            for c in range(n):
                if c in colSet or r+c in posDiag or r-c in negDiag:
                    continue
                
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
            
        backtrack(0)
        return res
                