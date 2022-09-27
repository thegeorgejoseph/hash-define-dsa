class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["*","/","+","-"])
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                temp = 0
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "*":
                    temp = (a*b)
                elif token == "+":
                    temp = (a+b)
                elif token == "-":
                    temp = (a-b)
                elif token == "/":
                    temp = int((a/b))
                stack.append(temp)
                
        return stack[-1]