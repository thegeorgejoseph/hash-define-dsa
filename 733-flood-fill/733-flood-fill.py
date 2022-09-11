class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        init_col = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c, init_col):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or image[r][c] == color or image[r][c] != init_col):
                return
            
            image[r][c] = color
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, init_col)
        
        dfs(sr,sc, init_col)
        return image