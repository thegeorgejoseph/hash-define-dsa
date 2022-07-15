class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = collections.deque([]) # pairs of [index, height]
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #after popping the height that cannot grow further we are moving current h backwar
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea