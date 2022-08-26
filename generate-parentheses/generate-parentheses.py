class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openBrackets, closedBrackets,s):
            if openBrackets == closedBrackets == n:
                res.append(s)
                return 
            if openBrackets < n:
                s += "("
                dfs(openBrackets + 1, closedBrackets,s)
                s = s[:-1]
            if closedBrackets < openBrackets:
                s += ")"
                dfs(openBrackets, closedBrackets + 1,s)
                s = s[:-1]
            
        
        dfs(0,0, "")
        return res