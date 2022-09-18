class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(word, openBracket, closedBracket):
            if openBracket == closedBracket == n:
                res.append(word)
                return
            if openBracket < n:
                dfs(word + "(", openBracket + 1, closedBracket)
            if closedBracket < openBracket:
                dfs(word + ")", openBracket, closedBracket + 1)
            
        dfs("", 0, 0)
        return res