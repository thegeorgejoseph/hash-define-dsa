class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        res = [-1,-1]
        length = float("inf")
        
        t_map, window = {}, {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        l = 0
        have, need = 0, len(t_map)
        for r in range(len(s)):
            char = s[r]
            if char in t_map:
                window[char] = window.get(char,0) + 1
                if window[char] == t_map[char]:
                    have += 1
            while have == need:
                if r - l + 1 < length:
                    length = r - l + 1
                    res = [l, r]
                    
                removeChar = s[l]
                if removeChar in t_map:
                    window[removeChar] -= 1
                    if window[removeChar] < t_map[removeChar]:
                        have -= 1
                
                l += 1
        left, right = res
        return s[left: right + 1] if length != float("inf") else ""