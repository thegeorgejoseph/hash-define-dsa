class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [sorted(tuple(w)) for w in strs]
        hashmap = defaultdict(list)
        
        for i,w in enumerate(sorted_strs):
            hashmap[tuple(w)].append(strs[i])
        
        return list(hashmap.values())