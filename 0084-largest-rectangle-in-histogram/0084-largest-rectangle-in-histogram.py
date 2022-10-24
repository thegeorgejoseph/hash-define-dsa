class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            currentIdx = i
            while stack and h < stack[-1][1]:
                prevIdx, prevHeight = stack.pop()
                res = max(res, (i - prevIdx)*prevHeight)
                currentIdx = prevIdx
            stack.append((currentIdx, h))
        while stack:
            i, h = stack.pop()
            res = max(res, (len(heights)-i)*h)
        return res