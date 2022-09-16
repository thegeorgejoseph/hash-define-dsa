class Solution:
    #for the love of god -- first check is "if" and second check is "while"
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
        return res