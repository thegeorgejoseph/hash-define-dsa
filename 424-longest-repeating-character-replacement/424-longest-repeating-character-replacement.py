from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #the windowlength - the maxFreq decides how many characters we need to replace in that window
        #update the windowLength after the left pointer changes
        # technically we do not have to update the maxFreq after the left pointer changes because we only
        # care when the maxFreq increases because that is what will have an effect on the solution
        # if we check the hashmap for largest each time left moves the time complexity becomes O(26*N)
        # if we do not check it becomes a pure O(N) solution
        cache = {}
        left, res = 0, 0
        maxFreq = 0
        for right in range(len(s)):
            windowLen = right - left + 1
            cache[s[right]] = 1 + cache.get(s[right],0)
            maxFreq = max(maxFreq, cache[s[right]])
            if (windowLen - maxFreq) > k:
                cache[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        