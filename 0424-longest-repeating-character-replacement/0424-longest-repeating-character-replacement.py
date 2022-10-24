class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        res, left, maxFreq = 0, 0, 0
        for right in range(len(s)):
            windowLength = right - left + 1
            cache[s[right]] = 1 + cache.get(s[right], 0)
            maxFreq = max(maxFreq, cache[s[right]])
            if windowLength - maxFreq > k:
                cache[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res