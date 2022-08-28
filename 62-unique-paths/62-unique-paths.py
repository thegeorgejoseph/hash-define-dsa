class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * n
        
        for i in range(m-1):
            currentRow = [1] * n
            for j in range(1,n):
                currentRow[j] = currentRow[j-1] + lastRow[j]
            lastRow = currentRow[:]
        
        return lastRow[-1]
            
        