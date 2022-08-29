class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m*n) - 1
        while left <= right:
            pivot = left + ((right - left) // 2)
            mid = matrix[pivot // n][pivot % n]
            if target < mid:
                right = pivot - 1
            elif target > mid:
                left = pivot + 1
            else:
                return True
        return False
        # m, n = len(matrix), len(matrix[0])
        # left, right = 0, m * n - 1
        # while left <= right:
        #     pivot = left + ((right - left) // 2)
        #     mid = matrix[pivot // n][pivot % n]
        #     if target == mid:
        #         return True
        #     if target > mid:
        #         left = pivot + 1
        #     else:
        #         right = pivot - 1
        # return False