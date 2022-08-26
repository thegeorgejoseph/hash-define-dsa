class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, part):
            if i == len(s):
                res.append(part[:])
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j):
                    part.append(s[i : j + 1])
                    dfs(j + 1, part)
                    part.pop()
        
        dfs(0, [])
        return res