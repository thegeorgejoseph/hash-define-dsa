class Solution:
    def houseRobber1(self, nums):
        rob1, rob2 = 0, 0
        for num in nums[::-1]:
            temp = rob2
            rob2 = max(num + rob1, rob2)
            rob1 = temp
        return rob2
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.houseRobber1(nums[:-1]), self.houseRobber1(nums[1:]))