class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(openBracket, closedBracket, bracket):
            if openBracket == closedBracket == n:
                res.append(bracket)
                return 
            
            if openBracket < n:
                dfs(openBracket + 1, closedBracket, bracket + "(")
            if closedBracket < openBracket:
                dfs(openBracket, closedBracket + 1, bracket + ")")
            
        
        
        dfs(0, 0, "")
        return res