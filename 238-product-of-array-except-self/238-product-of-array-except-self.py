class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = []
        for num in nums:
            res.append(prefix)
            prefix *= num
        prefix = 1
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            res[i] *= prefix
            prefix *= num
        return res
            