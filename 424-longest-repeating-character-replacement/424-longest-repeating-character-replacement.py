from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        left = 0
        res = 0
        maxf = 0
        for right in range(len(s)):
            cache[s[right]] = 1 + cache.get(s[right],0)
            maxf = max(maxf, cache[s[right]])
            if (right - left + 1 - maxf) > k:
                cache[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res