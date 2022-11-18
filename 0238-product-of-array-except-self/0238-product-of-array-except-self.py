class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num
        prefix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=prefix
            prefix*=nums[i]
        return res