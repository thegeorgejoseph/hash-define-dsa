class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = collections.deque([])
        
        def backtrack(openBrackets, closedBrackets):
            if openBrackets == closedBrackets == n :
                res.append("".join(stack))
                return
            if openBrackets < n:
                stack.append("(")
                backtrack(openBrackets + 1, closedBrackets)
                stack.pop()
            if closedBrackets < openBrackets:
                stack.append(")")
                backtrack(openBrackets, closedBrackets + 1)
                stack.pop()
            
        
        backtrack(0,0)
        return res