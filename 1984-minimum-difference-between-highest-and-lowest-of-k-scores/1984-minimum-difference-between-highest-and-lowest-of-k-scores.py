'''
Input: nums = [9,4,1,7], k = 2
Output: 2

Sorted nums = [1,4,7,9]

sliding window after
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        res = float('inf')
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res