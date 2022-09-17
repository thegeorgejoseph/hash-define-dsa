class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        initColor = image[sr][sc]
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or image[r][c] != initColor or image[r][c] == color):
                return 
            image[r][c] = color
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
        
        dfs(sr,sc)
        return image