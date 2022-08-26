class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentPrefix = 0
        res = nums[0]
        for num in nums:
            if currentPrefix < 0:
                currentPrefix = 0
            currentPrefix += num
            res = max(res, currentPrefix)
        return res