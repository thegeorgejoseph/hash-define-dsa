class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, perms):
            if len(nums) == 0:
                res.append(perms[:])
                return 
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], perms + [nums[i]])
        dfs(nums, [])
        return res