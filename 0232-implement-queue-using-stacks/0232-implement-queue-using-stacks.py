class MyQueue:

    def __init__(self):
        self.a, self.b = [], []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        self.peek()
        return self.b.pop()

    def peek(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        return len(self.a) == len(self.b) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()