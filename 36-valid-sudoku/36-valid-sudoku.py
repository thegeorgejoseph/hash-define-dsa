from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # pretty straight forward
        # just create default dicts because you need a default value for every key in it
        # neat
        rows = defaultdict(set)
        columns = defaultdict(set)
        cache = defaultdict(set) # key = (row //3 , col //3)
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if (curr in rows[i]) or (curr in columns[j]) or (curr in cache[(i // 3, j //3)]):
                    return False
                rows[i].add(curr)
                columns[j].add(curr)
                cache[(i // 3, j // 3)].add(curr)
        return True