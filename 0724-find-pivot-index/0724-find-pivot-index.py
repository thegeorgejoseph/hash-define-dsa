'''
Input: nums = [1,7,3,6,5,6]

'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l, r = 0, total - nums[0]
        if l == r: return 0
        prevIdx = 0
        for i in range(1, len(nums)):
            l += nums[prevIdx]
            r -= nums[i]
            prevIdx = i
            if l == r:
                return i
        return -1