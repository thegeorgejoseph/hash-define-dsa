class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea, stack = 0, []
        
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index)*height)
                idx = index
            stack.append((idx, h))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights)-i)*h)
        
        return maxArea