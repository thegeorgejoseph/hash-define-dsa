class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            p, pivot = left, nums[right]
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p == k:
                return nums[p]
            if k > p:
                left = p + 1
            else:
                right = p - 1
        return -1