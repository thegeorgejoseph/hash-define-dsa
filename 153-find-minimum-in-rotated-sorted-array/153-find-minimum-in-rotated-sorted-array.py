class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_val = float("inf")
        while left <= right:
            mid = left + ((right-left)>>1)
            min_val = min(nums[mid], min_val)
            if nums[left] <= nums[right]:
                return min(min_val, nums[left])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return min_val