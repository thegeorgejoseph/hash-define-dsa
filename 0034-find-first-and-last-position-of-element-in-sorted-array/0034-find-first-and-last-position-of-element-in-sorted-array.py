class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = float('inf'), float('-inf')
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right-left)//2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                first = min(first, mid)
                right = mid - 1
                
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right-left)//2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                last = max(last, mid)
                left = mid + 1
        if first == float('inf') and last == float('-inf'): return [-1,-1]
        return [first, last]