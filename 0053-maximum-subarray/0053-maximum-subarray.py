class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, prefix = float('-inf'), 0
        for num in nums:
            if prefix < 0:
                prefix = 0
            prefix += num
            res = max(res, prefix)
        return res