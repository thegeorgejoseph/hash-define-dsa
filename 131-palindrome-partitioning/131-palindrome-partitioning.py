class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(i, partition):
            if i == len(s):
                res.append(partition[:])
                return 
            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    backtrack(j + 1, partition)
                    partition.pop()
            
            
        backtrack(0, [])
        return res