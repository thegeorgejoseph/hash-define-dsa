class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(i, subset):
            if i == len(s):
                res.append(subset[:])
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i:j + 1])
                    backtrack(j + 1, subset)
                    subset.pop()
            
        backtrack(0, [])
        return res