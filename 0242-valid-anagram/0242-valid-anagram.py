class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache_s = [0]*26
        cache_t = [0]*26
        for char in s:
            cache_s[ord(char)-ord('a')] += 1
        for char in t:
            cache_t[ord(char)-ord('a')] += 1
        return cache_s == cache_t