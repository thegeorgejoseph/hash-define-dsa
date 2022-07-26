class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def houseRobber(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(houseRobber(nums[:-1]),houseRobber(nums[1:]))