class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                temp = matrix[top][left + i]
                
                matrix[top][top + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            left += 1
            right -= 1
        
        