class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = {}
        for c in text:
            if c in "balloon":
                have[c] = 1 + have.get(c, 0)
        for c in "balon":
            if c not in have: return 0
        need = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        _min = float('inf')
        for c in "balloon":
            _min = min(_min, have[c] // need[c])
        return _min
            
        