class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = float('-inf')
        for num in nums:
            if prefix < 0:
                prefix = 0
            prefix += num
            res = max(res, prefix)
        return res