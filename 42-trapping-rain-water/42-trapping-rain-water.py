class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        prefix_sum = []
        for h in height:
            prefix_sum.append(prefix)
            prefix = max(prefix, h)
        prefix = 0
        suffix_sum = []
        for h in height[::-1]:
            suffix_sum.append(prefix)
            prefix = max(prefix, h)
        suffix_sum = suffix_sum[::-1]
        res = 0
        for i, h in enumerate(height):
            minHeight = min(prefix_sum[i], suffix_sum[i])
            res += (minHeight-h) if (minHeight-h) > 0 else 0
        return res