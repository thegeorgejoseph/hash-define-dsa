class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cache = set(nums)
        for n in range(0, len(nums) + 1):
            if n not in cache:
                return n
        