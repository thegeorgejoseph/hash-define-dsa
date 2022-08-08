class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for word in strs:
            storage = [0] * 26
            for char in word:
                storage[ord(char) - ord('a')] += 1
            cache[tuple(storage)].append(word)
        return cache.values()