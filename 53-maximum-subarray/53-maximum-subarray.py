class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentPrefixSum = 0
        maxSoFar = nums[0]
        
        for n in nums:
            if currentPrefixSum < 0:
                currentPrefixSum = 0
            currentPrefixSum += n
            maxSoFar = max(currentPrefixSum, maxSoFar)
        
        return maxSoFar