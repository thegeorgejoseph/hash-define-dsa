# if t is empty return ""
# get the frequency of unique characters of t and the length of the map is the need
# have = 0, have gets incremented when frequency map of smap[char] == the same as that of tmap[char]
# when have == need, we try to reduce the window length


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        smap, tmap = {}, {}
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        have, need = 0, len(tmap)
        left, right = 0, 0
        res, length = [-1,-1], float('inf')
        while right < len(s):
            c = s[right]
            if c in tmap:
                smap[c] = smap.get(c, 0) + 1
                if smap[c] == tmap[c]:
                    have += 1
            while have == need:
                if right - left + 1 < length:
                    length = right - left + 1
                    res = [left, right]
                char = s[left]
                if char in tmap:
                    smap[char] -= 1
                    if smap[char] < tmap[char]:
                        have -= 1
                left += 1
            right += 1
        l, r = res
        return s[l: r + 1] if length != float('inf') else ""
                