class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        cache = defaultdict(list)
        for i,w in enumerate(words):
            pos = [0]*26
            for c in w:
                pos[ord(c)-ord('a')] += 1
            cache[i].append(pos)
        stack = []
        for i in range(len(words)):
            word = words[i]
            if i == 0 or cache[i-1] != cache[i]:
                stack.append(word)
            else:
                continue
        
        return stack