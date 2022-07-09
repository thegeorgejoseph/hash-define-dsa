from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # the letters should be the same in both the words
        # the count of the letters should be the same in both
        # early stopping criteria for speed : 
        # 1. if n != m then it cannot be an anagram
        # 2. if new letter not in the bank then it cannot be an anagram
        
        
        m, n = len(s), len(t)
        if m != n:
            return False
        
        counts = {}
        for char in s:
            counts[char] = 1 + counts.get(char, 0)
        
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True
        # Wrong interpretation of the question! Question asked for Anagram, I solved for Palindrome.
#         n = len(s)
#         m = len(t)
#         if n != m : 
#             return False
#         first = 0 
#         second = m - 1 # could have also been n, I guess.
        
#         while first < second : 
#             if s[first] != t[second]:
#                 return False
#             first += 1
#             second -= 1
        
#         return True