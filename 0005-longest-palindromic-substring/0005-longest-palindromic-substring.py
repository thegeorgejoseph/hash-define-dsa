class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = [-1,-1]
        
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = [left, right]
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = [left, right]
                left -= 1
                right += 1
    
        left, right = res
        if longest != 0:
            return s[left:right + 1]
        else:
            return ""
            