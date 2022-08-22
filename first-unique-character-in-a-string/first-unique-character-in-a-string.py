class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = [0] * 26
        for char in s:
            cache[ord(char)-ord('a')] += 1
        
        for i,char in enumerate(s):
            if cache[ord(char)-ord('a')] == 1:
                return i
        return -1