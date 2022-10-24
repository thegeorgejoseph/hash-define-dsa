class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            trapped = min(height[left], height[right])*(right-left)
            res = max(res, trapped)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res