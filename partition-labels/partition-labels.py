class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {}
        for i, char in enumerate(s):
            cache[char] = i
        
        maxIdx = cache[s[0]]
        res = []
        left = 0
        for i in range(1, len(s)):
            if i > maxIdx:
                res.append(maxIdx - left + 1)
                left = i
            maxIdx = max(maxIdx, cache[s[i]])
        res.append(maxIdx - left + 1)
        return res
            
                