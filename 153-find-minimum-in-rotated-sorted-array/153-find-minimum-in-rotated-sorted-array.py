class Solution:
    def findMin(self, nums: List[int]) -> int:
        # just like find element in rotated sorted array
        # left sorted array right sorted array type
        #check if left sorted array by nums[left] <= nums[mid]
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right :
            if nums[left] < nums[right]:
                #works because distinct elements
                res = min(res, nums[left])
                break
            mid = left + ((right - left) // 2)
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res