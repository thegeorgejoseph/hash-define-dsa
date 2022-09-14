class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         binary search requires the list to be sorted 
# find the middle element and then compare the target to the middle element
# if the target is smaller than the middle element then we only need to search the first half
# if the target is larger than the middle element then we need to search the second half
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            pivot = nums[mid]
            if target > pivot:
                left = mid + 1
            elif target < pivot:
                right = mid - 1
            else:
                return mid
        return -1