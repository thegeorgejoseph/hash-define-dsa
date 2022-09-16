class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target-total) < abs(diff):
                    diff = target - total
                if diff == 0: return target
                if total < target:
                    left += 1
                else:
                    right -= 1
        return target - diff