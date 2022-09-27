class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1,-1]
        longest = float('inf')
        if t == "":
            return ""
        t_cache = {}
        window = {}
        for c in t:
            t_cache[c] = 1 + t_cache.get(c, 0)
        need = len(t_cache)
        have = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in t_cache:
                window[char] = 1 + window.get(char, 0)
                if window[char] == t_cache[char]:
                    have += 1
            
            while have == need:
                if r - l + 1 < longest:
                    longest = r - l + 1
                    res = [l, r]
                char = s[l]
                if char in t_cache:
                    window[char] -= 1
                    if window[char] < t_cache[char]:
                        have -= 1
                
                l += 1
        l, r = res
        return s[l:r+1] if longest != float('inf') else ""
    
    
    