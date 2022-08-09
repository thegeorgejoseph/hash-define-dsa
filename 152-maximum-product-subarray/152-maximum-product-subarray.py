class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1,1
        res = nums[0]
        for n in nums:
            temp = n * curMin
            curMin = min(n, temp, n * curMax)
            curMax = max(n, temp, n * curMax)
            res = max(curMax, res)
        return res