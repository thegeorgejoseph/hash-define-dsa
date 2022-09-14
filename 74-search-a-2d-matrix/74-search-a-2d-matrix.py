class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS*COLS-1
        while left <= right:
            mid = left + ((right - left) // 2)
            pivot = matrix[mid // COLS][mid % COLS]
            if target < pivot:
                right = mid - 1
            elif target > pivot:
                left = mid + 1
            else:
                return True
        return False