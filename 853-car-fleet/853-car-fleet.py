class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars = [(position[i],speed[i]) for i in range(len(position))]
        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(key = lambda x: x[0])
        stack = collections.deque([])
        for d,s in pairs[::-1]:
            t = (target-d) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
            
        