class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, seq, farthest = 0, 0, 0, 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            seq += 1
        return seq