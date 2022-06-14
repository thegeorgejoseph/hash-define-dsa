class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque([])
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                a, b = int(stack.pop()),int(stack.pop())
                stack.append(int(b / a)) #integer division not floating point division
            else:
                stack.append(int(token))
        return stack.pop()