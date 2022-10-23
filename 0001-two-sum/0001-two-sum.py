class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                return [i, cache[nums[i]]]
            cache[target-nums[i]] = i
        return -1
                
        