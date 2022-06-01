from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # the letters should be the same in both the words
        # the count of the letters should be the same in both
        # early stopping criteria for speed : 
        # 1. if n != m then it cannot be an anagram
        # 2. if new letter not in the bank then it cannot be an anagram
        
        
        n = len(s)
        m = len(t)
        if n != m :
            return False
        
        letter_bank  = defaultdict(lambda: 0) # defaultdict spec from docs
        for letter in s : 
            letter_bank[letter] += 1
            
        for letter in t:
             if letter not in letter_bank:
                    return False
             else:
                if letter_bank[letter] == 0:
                    return False
                letter_bank[letter] -= 1
                
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