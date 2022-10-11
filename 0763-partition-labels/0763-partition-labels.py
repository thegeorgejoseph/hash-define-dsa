class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}
        res = []
        l = 0
        maxIdx = lastIdx[s[0]]
        for r in range(1, len(s)):
            if r > maxIdx:
                res.append(maxIdx - l + 1)
                l = r
            maxIdx = max(maxIdx, lastIdx[s[r]])
        res.append(r-l+1)
        return res