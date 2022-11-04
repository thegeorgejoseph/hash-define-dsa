'''
Input: nums = [2,3,-2,4, -1]
Output: 6

curMin = 2 ,3, -12, -48, -4
curMax = 2, 6, -2, 4, 48

[3,-2,4]
res = 6
use temp to store curMin
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMin, curMax = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            temp = curMin
            curMin = min(num, num * curMin, num * curMax)
            curMax = max(num, num * temp, num * curMax)
            res = max(res, curMax)
        return res