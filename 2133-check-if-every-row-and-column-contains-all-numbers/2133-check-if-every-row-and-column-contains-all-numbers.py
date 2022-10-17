class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]: return False
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        # for i in range(1,len(matrix)+1):
        #     if len(rows[i]) != len(matrix) or len(cols[i]) != len(matrix): return False
        return True