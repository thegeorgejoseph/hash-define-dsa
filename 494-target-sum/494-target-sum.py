class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in cache:
                return cache[(i,total)]
            
            res = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            cache[(i, total)] = res
            return res
            
        return dfs(0,0)
#         cache = {}
        
#         def dfs(i, t):
#             if i == len(nums):
#                 return 1 if t == target else 0
#             if (i,t) in cache:
#                 return cache[(i,t)]
            
#             cache[(i,t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
#             return cache[(i,t)]   
        
#         return dfs(0,0)