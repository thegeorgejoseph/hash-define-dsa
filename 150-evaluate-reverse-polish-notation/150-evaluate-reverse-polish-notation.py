class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque([])
        for token in tokens:
            if token == "+":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(str(a + b))
            elif token == "-":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(str(a - b))
            elif token == "*":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(str(a * b))
            elif token == "/":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(token)
        return int(stack.pop())