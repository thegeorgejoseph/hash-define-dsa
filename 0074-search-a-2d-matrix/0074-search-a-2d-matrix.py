class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l,r = 0, (m*n)-1
        while l <= r:
            mid = l + ((r-l)>>1)
            val = matrix[mid//n][mid%n]
            if val == target:
                return True
            if target < val:
                r = mid - 1
            else:
                l = mid + 1
        return False