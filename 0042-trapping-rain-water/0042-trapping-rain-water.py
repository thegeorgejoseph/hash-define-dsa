class Solution:
    def trap(self, height: List[int]) -> int:
        leftHeights = []
        prefix = 0
        for h in height:
            leftHeights.append(prefix)
            prefix = max(prefix, h)
        rightHeights = []
        suffix = 0
        for h in height[::-1]:
            rightHeights.append(suffix)
            suffix = max(suffix, h)
        rightHeights = rightHeights[::-1]
        res = 0
        for i in range(len(height)):
            res += min(leftHeights[i], rightHeights[i])-height[i] if min(leftHeights[i], rightHeights[i])-height[i] > 0 else 0
        return res