class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            pivot = left + ((right - left)//2)
            element = matrix[pivot // n][pivot % n] #divide by number of columns
            if element == target:
                return True
            elif element < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return False