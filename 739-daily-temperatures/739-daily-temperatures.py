class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack  = deque()
        res = [0] * (len(temperatures))
        
        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                top, i = stack.pop()
                res[i] = idx - i
            
            stack.append((temp, idx))
        
        return res