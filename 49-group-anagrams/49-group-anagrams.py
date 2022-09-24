class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c)-ord('a')] += 1
            cache[tuple(temp)].append(word)
        return list(cache.values())