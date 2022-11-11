class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for w in strs:
            pos = [0]*26
            for c in w:
                pos[ord(c)-ord('a')] += 1
            cache[tuple(pos)].append(w)
        return list(cache.values())
            