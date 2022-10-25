'''
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

sum(nums) -> 22
sum(subset) -> 11
[(1),(0),(6),(5),(0),(11)]

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

sum(nums) -> 11

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            total = total // 2
        
        cache = set([0])
        for num in nums:
            for n in cache.copy():
                if n + num == total:
                    return True
                cache.add(n + num)
        return False