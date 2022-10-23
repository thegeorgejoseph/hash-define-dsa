class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            pivot = left + ((right-left)//2)
            middle = matrix[pivot//n][pivot%n]
            if target == middle:
                return True
            if target < middle:
                right = pivot - 1
            elif target > middle:
                left = pivot + 1
        return False