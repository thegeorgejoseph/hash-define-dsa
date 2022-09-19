class FreqStack:

    def __init__(self):
        self.counter = {} # val : freq
        self.max = 0
        self.stacks = {} # freq : [val1, val2, val3]

    def push(self, val: int) -> None:
        count = self.counter.get(val, 0) + 1
        self.counter[val] = count
        if count > self.max:
            self.max = count
            self.stacks[count] = []
        self.stacks[count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max].pop()
        self.counter[res] -= 1
        if not self.stacks[self.max]:
            self.max -= 1
        return res