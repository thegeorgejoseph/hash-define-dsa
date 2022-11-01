'''
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
[[1]]
newRow is of size res[-1] + 1
temp array can hold [0] + res[-1] + [0]
iterate through every pair to get the new row
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            prevRow = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(prevRow[j] + prevRow[j + 1])
            res.append(row)
        return res