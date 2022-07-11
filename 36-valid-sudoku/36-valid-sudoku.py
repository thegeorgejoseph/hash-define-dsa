from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # pretty straight forward
        # just create default dicts because you need a default value for every key in it
        # neat
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        cache = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if (curr in ROWS[i] or curr in COLS[j] or curr in cache[(i // 3, j // 3)]):
                    return False
                ROWS[i].add(curr)
                COLS[j].add(curr)
                cache[(i // 3, j // 3)].add(curr)
        return True