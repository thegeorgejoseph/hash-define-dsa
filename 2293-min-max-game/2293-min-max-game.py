class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        controller = False
        while len(nums) > 1:
            temp = []
            for i in range(0, len(nums), 2):
                if controller:
                    temp.append(max(nums[i],nums[i+1]))
                else:
                    temp.append(min(nums[i], nums[i+1]))
                controller = not controller
            nums = temp
        return nums[0]