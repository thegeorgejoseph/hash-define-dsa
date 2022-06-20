class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                #base case you need to append to res
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res