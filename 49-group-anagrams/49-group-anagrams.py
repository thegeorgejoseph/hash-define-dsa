class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for word in strs:
            salt = [0] * 26
            for c in word:
                salt[ord(c)-ord('a')] += 1
            cache[tuple(salt)].append(word)
        return list(cache.values())
        
        
#         sorted_strs = [sorted(tuple(w)) for w in strs]
#         hashmap = defaultdict(list)
        
#         for i,w in enumerate(sorted_strs):
#             hashmap[tuple(w)].append(strs[i])
        
#         return list(hashmap.values())