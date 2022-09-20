class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            startIdx = i
            while stack and stack[-1][1] > h:
                prevIdx, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight*(i - prevIdx))
                startIdx = prevIdx
            stack.append((startIdx, h))
        
        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, height*(len(heights)-idx))
        return maxArea
        