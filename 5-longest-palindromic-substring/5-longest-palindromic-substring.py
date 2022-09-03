class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, left, right = 0, 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    longest = length
                    left, right = l, r
                l, r = l - 1, r + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    longest = length
                    left, right = l, r
                l, r = l - 1, r + 1
        return s[left: right + 1]