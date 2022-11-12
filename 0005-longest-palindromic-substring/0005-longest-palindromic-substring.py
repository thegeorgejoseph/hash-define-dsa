class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        ans = [None, None]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1 
                    ans = [l,r]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1 
                    ans = [l,r]
                l -= 1
                r += 1
        l, r = ans
        return s[l : r + 1] if res != 0 else ""