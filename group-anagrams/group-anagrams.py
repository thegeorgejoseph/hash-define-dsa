class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            hashes = [0] * 26
            for c in word:
                hashes[ord(c) - ord('a')] += 1
            hashmap[tuple(hashes)].append(word)
        
        return list(hashmap.values())
#         sorted_strs = [sorted(tuple(w)) for w in strs]
#         hashmap = defaultdict(list)
        
#         for i,w in enumerate(sorted_strs):
#             hashmap[tuple(w)].append(strs[i])
        
#         return list(hashmap.values())