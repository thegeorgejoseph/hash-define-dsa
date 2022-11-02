class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_cache, s_cache = {}, {}
        words = s.split()
        if len(pattern) != len(words): return False
        for c, word in zip(pattern, words):
            if (c in p_cache and p_cache[c] != word) or (word in s_cache and s_cache[word] != c):
                return False
            p_cache[c] = word
            s_cache[word] = c
        return True