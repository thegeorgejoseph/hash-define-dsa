class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cache = set(nums)
        for num in range(0, len(nums)+1):
            if num not in cache:
                return num
        