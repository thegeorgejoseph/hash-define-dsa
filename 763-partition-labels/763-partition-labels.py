class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {}
        for i in range(len(s)):
            cache[s[i]] = i
        maxIdx = cache[s[0]]
        left = 0
        res = []
        for i in range(1, len(s)):
            if i > maxIdx:
                res.append(maxIdx - left + 1)
                left = i
            maxIdx = max(maxIdx, cache[s[i]])
        res.append(maxIdx - left + 1)
        return res