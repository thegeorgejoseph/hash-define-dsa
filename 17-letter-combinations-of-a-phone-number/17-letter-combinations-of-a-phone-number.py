class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
             "2": "abc",
            "3": "def",
            "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz"
        }
        
        def dfs(i, string):
            if i == len(digits):
                res.append(string)
                return 
            for char in mapping[digits[i]]:
                string += char
                dfs(i + 1, string)
                string = string[:-1]
            
        if digits: dfs(0, "")
        return res