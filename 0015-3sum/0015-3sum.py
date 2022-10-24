class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
        return res