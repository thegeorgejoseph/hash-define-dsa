'''
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Counting Sort Technique - three variables to hold the counts of each value
Iterate over the array and replace accordingly
Two Pass

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
        """
        Do not return anything, modify nums in-place instead.
        """
        cache = {0 : 0, 1: 0, 2: 0}
        for num in nums:
            cache[num] += 1
        idx = 0
        for key, value in cache.items():
            for i in range(value):
                nums[idx] = key
                idx += 1
        
        