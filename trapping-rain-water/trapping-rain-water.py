class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        prefix_sum = []
        for h in height:
            prefix_sum.append(prefix)
            prefix = max(prefix, h)
        suffix = 0
        suffix_sum = []
        for h in height[::-1]:
            suffix_sum.append(suffix)
            suffix = max(suffix, h)
        suffix_sum = suffix_sum[::-1]
        cap = 0
        for i in range(len(height)):
            cap += min(prefix_sum[i], suffix_sum[i]) - height[i] if min(prefix_sum[i], suffix_sum[i]) - height[i] > 0 else 0
        return cap