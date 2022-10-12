class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(target-total) < abs(diff):
                    diff = target - total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return target - diff