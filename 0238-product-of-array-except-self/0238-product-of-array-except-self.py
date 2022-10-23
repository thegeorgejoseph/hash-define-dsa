# ```

# [1,2,3,4]
# [1,1, 2, 6]
# [  24  ,12 ,8 , 6]


# ```

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = []
        for num in nums:
            res.append(prefix)
            prefix *= num
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res