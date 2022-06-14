class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque([])
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            # if len(stack) > 0 and t > stack[-1][0]:
            while len(stack) > 0 and t > stack[-1][0]:
                topValue, topIdx = stack.pop()
                res[topIdx] = i - topIdx
            stack.append((t,i))
        return res