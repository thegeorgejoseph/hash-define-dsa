class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        cache = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return 
            
            num = digits[i]
            for word in cache[num]:
                for c in word:
                    s += c
                    dfs(i + 1, s)
                    s = s[:-1]
                
            
            
        dfs(0, "")
        return res