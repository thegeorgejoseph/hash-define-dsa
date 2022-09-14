class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        prefix_height = [0] * (len(height))
        for i in range(len(height)):
            prefix_height[i] = prefix
            prefix = max(prefix, height[i])
        suffix = 0
        suffix_height = [0] * (len(height))
        for i in range(len(height)-1,-1,-1):
            suffix_height[i] = suffix
            suffix = max(suffix, height[i])
        res = 0
        for i in range(len(height)):
            res += min(prefix_height[i],suffix_height[i]) - height[i] if min(prefix_height[i],suffix_height[i]) - height[i] > 0 else 0
        return res