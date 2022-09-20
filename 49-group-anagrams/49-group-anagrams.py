class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for word in strs:
            key = sorted(word)
            cache[tuple(key)].append(word)
        return list(cache.values())
#         cache =  defaultdict(list)
#         for word in strs:
#             temp = [0]*26
#             for char in word:
#                 temp[ord(char)-ord('a')] += 1
#             cache[tuple(temp)].append(word)
#         return list(cache.values())
# #         sorted_strs = [sorted(tuple(w)) for w in strs]
#         hashmap = defaultdict(list)
        
#         for i,w in enumerate(sorted_strs):
#             hashmap[tuple(w)].append(strs[i])
        
#         return list(hashmap.values())