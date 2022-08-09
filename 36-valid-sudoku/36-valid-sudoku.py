from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        valid = "123456789"
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        quad_set = defaultdict(set)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                if (board[i][j] not in valid or board[i][j] in row_set[i] or
                    board[i][j] in col_set[j] or board[i][j] in quad_set[(i // 3, j // 3)]):
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                quad_set[(i // 3, j // 3)].add(board[i][j])
        return True
    
    
    
# we need a set to keep track of each row and column - map of sets? - defaultdict(set)
# we need a set to keep track of the divided part of the board - (i // 3, j // 3)
# double for loop and create the sets 
#  anytime something is not "." check
# if it is in between 1-9, and if it is not not there in the sets then add it to the sets, but if it is there in the sets return False
# if it works return True