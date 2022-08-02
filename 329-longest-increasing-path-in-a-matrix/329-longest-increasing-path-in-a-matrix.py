class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r,c,prev):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or prev >= matrix[r][c]):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res, dfs(r + 1,c, matrix[r][c]) + 1)
            res = max(res, dfs(r,c + 1, matrix[r][c]) + 1)
            res = max(res, dfs(r - 1,c, matrix[r][c]) + 1)
            res = max(res, dfs(r,c - 1, matrix[r][c]) + 1)
            
            dp[(r,c)] = res
            return res
        
        LIP = 1
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r,c,-1))
        
        return LIP