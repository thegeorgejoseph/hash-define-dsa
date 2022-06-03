class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         binary search requires the list to be sorted 
# find the middle element and then compare the target to the middle element
# if the target is smaller than the middle element then we only need to search the first half
# if the target is larger than the middle element then we need to search the second half
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2 ) # (right + left) // 2 can lead to overflow of 32 bit integers
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1