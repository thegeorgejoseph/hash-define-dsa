class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using enumerate probably increase the space time complexity so use it sparingly
        
        visit = {}
        for i in range(len(nums)):
            if target - nums[i] in visit:
                return [i, visit[target-nums[i]]]
            visit[nums[i]] = i
        return [-1,-1]
        
        
        
        
        
#         double for loop method: iterate over every element twice and check if the sum of those two elements equal the target results in O(n**2) time space complexity.
# hashing method: if you hash the target - current element while iterating the list then when you see an element that is present in the hash set it means that the two sum exists - O(n) time space
# sorting method: sort the elements in O(nlogn) time and two pointer approach from back and front results in a O(nlogn) time O(n) space approach which is worse than method 2

        # remainder = {}
        # for idx, num in enumerate(nums):
        #     if num in remainder:
        #         return [remainder[num],idx]
        #     remainder[target - num] = idx
        # else: 
        #     return [-1,-1]