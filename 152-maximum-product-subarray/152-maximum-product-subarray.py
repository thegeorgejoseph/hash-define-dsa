class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = curMin = curMax = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = curMin
            curMin = min(n, n * curMin, n * curMax)
            curMax = max(n, n * temp, n * curMax)
            res = max(res, curMax)
        
        return res