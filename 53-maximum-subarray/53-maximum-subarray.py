class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentPrefixSum = 0
        res = nums[0]
        for num in nums:
            if currentPrefixSum < 0:
                currentPrefixSum = 0
            currentPrefixSum += num
            res = max(res, currentPrefixSum)
        return res