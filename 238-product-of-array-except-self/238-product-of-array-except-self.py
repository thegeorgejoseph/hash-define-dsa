class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum  = []
        prefix = 1
        for num in nums:
            prefix_sum.append(prefix * num)
            prefix = prefix * num
        suffix_sum = []
        suffix = 1
        for num in nums[::-1]:
            suffix_sum.append(suffix * num)
            suffix = suffix * num
        suffix_sum = suffix_sum[::-1]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_sum[i+1])
            elif i == len(nums)-1:
                res.append(prefix_sum[i-1])
            else:
                res.append(prefix_sum[i-1]*suffix_sum[i+1])
        return res