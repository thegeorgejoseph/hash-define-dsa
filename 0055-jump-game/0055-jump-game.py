class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        targetIdx = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= targetIdx:
                targetIdx = i
                nums[i] = True
            else:
                nums[i] = False
        return nums[0]
            