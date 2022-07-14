class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left, right, res = 0, 0, 0
        n = len(s)
        while right < n:
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            res = max(res, right - left + 1)
            hashset.add(s[right])
            right += 1
        return res