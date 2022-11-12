class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            temp = curMin
            curMin = min(nums[i], curMin*nums[i], curMax*nums[i])
            curMax = max(nums[i], temp*nums[i], curMax*nums[i])
            res = max(res, curMax)
        
        return res