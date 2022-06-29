class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1
        for i in range(n -1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return True if target == 0 else False
        # This solution works but it will TLE
#         n = len(nums)
#         dp = [False] * (len(nums))
#         dp[len(nums)-1] = True
#         for i in range(len(nums)-1,-1,-1):
#             for j in range(nums[i]+1):
#                 if i + j <= n and dp[i + j] == True:
#                     dp[i] = True
#                     break
            
#         return dp[0]