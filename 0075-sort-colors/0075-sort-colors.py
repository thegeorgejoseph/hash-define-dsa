'''
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Counting Sort Technique - three variables to hold the counts of each value
Iterate over the array and replace accordingly
Two Pass

cache = {0 : 0, 1: 0, 2: 0}
        for num in nums:
            cache[num] += 1
        idx = 0
        for key, value in cache.items():
            for i in range(value):
                nums[idx] = key
                idx += 1
        
        
Quick Sort Partition Method 
Left Ptr holds the 0 boundary
Right Ptr holds the 2 boundary
swap nums[left] nums[i] when i points to 0
swap nums[right] and nums[i] when i points to 2
increment i if left is swapped or when nums[i] is 1
do not increment i if right is swapped because there could be a 1 on the left
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        
        
        
        