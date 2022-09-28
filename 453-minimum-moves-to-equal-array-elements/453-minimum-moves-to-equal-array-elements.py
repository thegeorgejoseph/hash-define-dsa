class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = min(nums)
        res = 0
        for n in nums:
            res += n - _min
        return res