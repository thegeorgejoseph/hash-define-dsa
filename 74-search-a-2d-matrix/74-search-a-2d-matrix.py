class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            pivot = left + ((right - left)>>1)
            mid = matrix[pivot //n][pivot%n]
            if mid == target:
                return True
            if target < mid:
                right = pivot - 1
            else:
                left = pivot + 1
        return False
        