'''
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

 **contiguous non-empty subarray
 **return the product.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

[-2,1,-4] -> 8
with our logic we will return 1

curMin = [-2,-2,-4] -> use temp not to update curMin preemptively
curMax = [-2,1,8]  -> result comes from here
min-max(num*curMin, num*curMax, num)
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax, res = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            temp = curMin
            curMin = min(curMin*nums[i], curMax*nums[i], nums[i])
            curMax = max(temp*nums[i], curMax*nums[i], nums[i])
            res = max(res, curMax)
        return res