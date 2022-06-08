class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         negative prefixes are pointless
        max_so_far = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                 currentSum = 0
            currentSum += n
            max_so_far = max(max_so_far, currentSum)
            
        return max_so_far