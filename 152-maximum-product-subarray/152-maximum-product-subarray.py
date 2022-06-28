class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = float("-inf")
        for n in nums:
            temp = n * curMax # don't want to use updated curMax for curMin calculation
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, temp, n * curMin)
            res = max(res, curMax)
        return res