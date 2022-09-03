class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openBracket, closedBracket, s):
            if openBracket == closedBracket == n:
                res.append(s)
                return
            if openBracket < n:
                backtrack(openBracket + 1, closedBracket, s + '(')
            if closedBracket < openBracket:
                backtrack(openBracket, closedBracket + 1, s + ')')
            
        backtrack(0,0, "")
        return res