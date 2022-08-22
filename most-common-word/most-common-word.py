class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalised_string = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalised_string.split()
        banned_set = set(banned)
        hashmap = defaultdict(int)
        
        for word in words:
            if word not in banned_set:
                hashmap[word] += 1
        
        max_value = max(hashmap.values())
        
        for key, value in hashmap.items():
            if value == max_value:
                return key
            
        