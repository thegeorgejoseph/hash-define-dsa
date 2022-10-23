class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = float('inf')
        k = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                return min(res, nums[left])
            mid = left + ((right-left)//2)
            if nums[mid] < res:
                res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res