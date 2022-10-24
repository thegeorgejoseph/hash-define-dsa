class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_sum = []
        prefix = 0
        for i in range(len(height)):
            prefix = max(prefix, height[i])
            prefix_sum.append(prefix)
        prefix = 0
        postfix_sum = []
        for i in range(len(height)-1,-1,-1):
            prefix = max(prefix, height[i])
            postfix_sum.append(prefix)
        postfix_sum = postfix_sum[::-1]
        res = 0
        for i in range(len(prefix_sum)):
            res += (min(prefix_sum[i], postfix_sum[i]) - height[i]) if (min(prefix_sum[i], postfix_sum[i]) - height[i]) >= 0 else 0
        return res
            