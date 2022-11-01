'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

[3,2,2,3]
l

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1
        count  = 0
        for num in nums:
            if num != val: count += 1
        return count