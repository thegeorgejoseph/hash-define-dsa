class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return 
            dfs(i + 1, subset)
            dfs(i + 1, subset + [nums[i]])
            return
        dfs(0, [])
        return res