class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(height[left],height[right]))
            if height[left] > height[right]:
                right -= 1
                continue
            left += 1
        return res