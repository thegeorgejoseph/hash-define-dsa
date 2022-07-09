class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         [1,2,3,4]
#         [24,12,8,6]
#         prefix = [1,2,6,24]
#         postfix = [24,24,12,4]
#         res = [24,12,8,6]
        
#         res = [1,1,2,6]
#               [24,12,8,6]
#         most annoying question so far
#         basically the iterative approach is easy to follow, make prefix and postfix and then
#         just for every answer position multiply the prefix with the postfix and voila
#         but for the "smarter" solution it is different
#         we build the result array with the NOT the prefixes that you compute for the easy answer
#         but the prefix thus far
#         and then multiply with the postfixes
            n = len(nums)
            res = [1] * n
            prefix = 1
            for i in range(n):
                res[i] = prefix
                prefix *= nums[i]
            postfix = 1
            for i in range(n - 1, -1, -1):
                res[i] *= postfix
                postfix *= nums[i]
            return res
#         #Logic approach to solving the problem
#         #Get Prefix List and Suffix List, Handle Edge Cases
#         #For every element the result is the multiplication of its prefix and suffix
#         #For beginning and ending the prefix/ suffix is equal to 1
#         prefix = [1 for i in range(len(nums))]
#         suffix = [1 for i in range(len(nums))]
#         prefix[0] = nums[0]
#         suffix[0] = nums[-1]
#         for i in range(1, len(nums)):
#             prefix[i] = prefix[i-1] * nums[i]
#         for i in range(1, len(nums)):
#             print(suffix[i-1], nums[i])
#             suffix[i] = suffix[i-1] * nums[len(nums) - 1- i]
#         suffix.reverse()
#         res = [1 for _ in range(len(nums))]
#         for i in range(len(nums)):
#             if i == 0:
#                 res[i] = 1 * suffix[i+1]
#                 continue
#             if i == len(nums) - 1:
#                 res[i] = 1 * prefix[i-1]
#                 continue
#             res[i] = prefix[i-1] * suffix[i+1]
            
#         return res