class Solution:
    def findSumOfSquares(self, n):
        result = 0 
        while n: 
            result += (n  % 10) ** 2
            n = n // 10
        return result
    def isHappy(self, n: int) -> bool:
#         Mathematics way of doing it!
#         the thing loops forever, whether or not you get the happy nyumber or not. so essentally this is a hash set problem because we are just looking for numbers that has already been visited before, and we do not want to keep repeating it!

        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = self.findSumOfSquares(n)
            
        return False
            