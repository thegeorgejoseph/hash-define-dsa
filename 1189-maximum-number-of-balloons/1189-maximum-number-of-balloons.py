class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = Counter("balloon")
        have = Counter(text)
        res = float('inf')
        for c in "balon":
            if c not in have: return 0
            res = min(res, have[c]//need[c])
        return res
            