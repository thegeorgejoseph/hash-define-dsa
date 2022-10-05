class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = min(nums)
        res = 0
        for num in nums:
            res += num - _min
        return res