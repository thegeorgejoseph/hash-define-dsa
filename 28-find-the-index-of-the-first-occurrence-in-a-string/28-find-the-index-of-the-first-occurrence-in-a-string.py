class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i, c in enumerate(haystack):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1