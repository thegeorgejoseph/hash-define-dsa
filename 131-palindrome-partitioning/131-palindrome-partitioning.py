class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, parts):
            if i == len(s):
                res.append(parts[:])
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    parts.append(s[i:j+1])
                    dfs(j + 1, parts)
                    parts.pop()
            
        
        dfs(0, [])
        return res
        
        
        
        
        