class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
#         nums.append(0)
#         nums.append(0)
        
#         for i in range(len(nums) - 3, -1, -1):
#             nums[i] = max(nums[i]  + nums[i + 2], nums[i + 1])
        
#         return nums[0]