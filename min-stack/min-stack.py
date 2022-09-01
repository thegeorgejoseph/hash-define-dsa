class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            _min = val
        else:
            _min = min(val, self.stack[-1][1])
        self.stack.append((val, _min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()