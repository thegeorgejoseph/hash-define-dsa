class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        cache = set()
        while right < len(s):
            if s[right] not in cache:
                cache.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                cache.remove(s[left])
                left += 1
        return res