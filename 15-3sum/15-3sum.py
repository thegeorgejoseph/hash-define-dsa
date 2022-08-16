class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] < 0:
                    left += 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res