class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalised_string = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalised_string.split()
        banned = set(banned)
        freqs = {}
        
        for word in words:
            if word not in banned:
                freqs[word] = 1 + freqs.get(word, 0)
        
        max_val = max(freqs.values())
        for key, val in freqs.items():
            if val == max_val: return key
        
        