class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def houseRobber(nums):
            rob1, rob2 = 0,0 
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2 
                rob2 = temp
            return temp
        
        return max(houseRobber(nums[:-1]),houseRobber(nums[1:]))