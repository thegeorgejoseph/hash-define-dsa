class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counts = {}
        for i, c in enumerate(s):
            counts[c] = i
            
        maxIdx = counts[s[0]]
        left = 0
        for i in range(len(s)):
            if i > maxIdx:
                res.append(maxIdx - left + 1 )
                left = maxIdx + 1
            maxIdx = max(maxIdx, counts[s[i]])
        
        res.append(maxIdx - left + 1)
        return res
