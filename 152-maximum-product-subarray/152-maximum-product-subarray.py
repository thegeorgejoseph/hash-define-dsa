class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curMin,curMax = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = n * curMin
            curMin = min(n, temp, n * curMax)
            curMax = max(n, temp, n * curMax)
            res = max(res, curMax)
        return res