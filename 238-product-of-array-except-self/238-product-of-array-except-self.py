class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Logic approach to solving the problem
        #Get Prefix List and Suffix List, Handle Edge Cases
        #For every element the result is the multiplication of its prefix and suffix
        #For beginning and ending the prefix/ suffix is equal to 1
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        prefix[0] = nums[0]
        suffix[0] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(1, len(nums)):
            print(suffix[i-1], nums[i])
            suffix[i] = suffix[i-1] * nums[len(nums) - 1- i]
        suffix.reverse()
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1 * suffix[i+1]
                continue
            if i == len(nums) - 1:
                res[i] = 1 * prefix[i-1]
                continue
            res[i] = prefix[i-1] * suffix[i+1]
            
        return res