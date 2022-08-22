class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap method
        cache = {}
        for i, num in enumerate(nums):
            if num in cache:
                return [i, cache[num]]
            cache[target-num] = i
        return [-1,-1]