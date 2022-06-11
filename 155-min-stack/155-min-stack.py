class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
             self.stack.append((val,val))
        else:
            minVal = self.stack[-1][1]
            if val < minVal:
                minVal = val
            self.stack.append((val,minVal))
        return self.stack
    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        top = self.stack[-1][0]
        return top

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        top = self.stack[-1][1]
        return top


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()