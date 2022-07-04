class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1
        
        while left < right:
            top, bottom = left, right
            #top and bottom going up and down is updated with the above statement
            for i in range(right - left):
                topLeft = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top+ i][right] = topLeft
                
            left += 1
            right -= 1
        