class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque([])
        res = [0] * (len(temperatures))
        
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((t,i))
        
        return res