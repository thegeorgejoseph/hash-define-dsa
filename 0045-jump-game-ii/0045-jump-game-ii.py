[2,3,1,1,4]
[2, 3, 0, 1, 4]
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*(len(nums))
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            jump = nums[i]
            for j in range(jump+1):
                if i + j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]