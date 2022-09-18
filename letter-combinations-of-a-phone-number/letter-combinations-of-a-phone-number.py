class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        cache = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        res = []
        def dfs(i, word):
            if i == len(digits):
                res.append(word)
                return 
            for c in cache[digits[i]]:
                word += c
                dfs(i + 1, word)
                word = word[:-1]

        dfs(0, "")
        return res