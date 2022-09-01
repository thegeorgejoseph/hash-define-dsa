class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for idx, num in enumerate(nums):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if diff == 0:
                    return target
                if total > target:
                    right -= 1
                else:
                    left += 1
         
        return target - diff