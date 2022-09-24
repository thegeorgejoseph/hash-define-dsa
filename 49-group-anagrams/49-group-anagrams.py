class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = "akshata"
        cache = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            cache[key].append(word)
        return list(cache.values())
        
        # cache = defaultdict(list)
        # for word in strs:
        #     temp = [0] * 26
        #     for c in word:
        #         temp[ord(c)-ord('a')] += 1
        #     cache[tuple(temp)].append(word)
        # return list(cache.values())