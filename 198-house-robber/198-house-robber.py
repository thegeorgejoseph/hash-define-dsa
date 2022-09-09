class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, nums[0]
        for i in range(1, len(nums)):
            temp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            rob1 = temp
        return rob2
#         nums.append(0)
#         for i in range(len(nums)-3,-1,-1):
#             nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        
#         return nums[0]