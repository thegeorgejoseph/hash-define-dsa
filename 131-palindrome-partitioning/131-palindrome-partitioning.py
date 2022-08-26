class Solution:
    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, part):
            if i == len(s):
                res.append(part[:])
                return 
            
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1, part)
                    part.pop()
            
            
        
        dfs(0, [])
        return res