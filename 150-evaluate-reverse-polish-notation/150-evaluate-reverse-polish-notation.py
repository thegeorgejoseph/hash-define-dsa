class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                two = int(stack.pop())
                one = int(stack.pop())
                if token == "+":
                    stack.append(one + two)
                elif token ==  "-":
                    stack.append(one - two)
                elif token ==  "*":
                    stack.append(one * two)
                elif token ==  "/":
                    stack.append(int(one / two))
            else:
                stack.append(token)
        return stack[-1]
                    