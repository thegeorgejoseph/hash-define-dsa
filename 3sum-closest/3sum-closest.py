class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for idx, num in enumerate(nums):
            left, right = idx + 1, len(nums) -1 
            while left < right:
                _sum = num + nums[left] + nums[right]
                if abs(target - _sum) < abs(diff):
                    diff = target - _sum
                if _sum < target:
                    left += 1
                else:
                    right -= 1
                if diff == 0:
                    break
        return target - diff