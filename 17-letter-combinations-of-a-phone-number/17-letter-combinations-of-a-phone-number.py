class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        cache = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def dfs(i, word):
            if i == len(digits):
                res.append(word)
                return 
            
            possible = cache[digits[i]]
            for j in range(len(possible)):
                word += possible[j]
                dfs(i + 1, word)
                word = word[:-1]
            
        dfs(0, "")
        return res