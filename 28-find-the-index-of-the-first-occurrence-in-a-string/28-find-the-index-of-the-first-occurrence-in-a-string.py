class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i, c in enumerate(haystack):
            if c == needle[0] and haystack[i: i + len(needle)] == needle:
                return i
        return -1