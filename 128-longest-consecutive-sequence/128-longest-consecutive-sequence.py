class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = {}
        for num in nums:
            visit[num] = False
        res = 0
        for num in nums:
            left = num - 1
            seq = 1
            visit[num] = True
            while left in visit and visit[left] != True:
                visit[left] = True
                left -= 1
                seq += 1
            right = num + 1
            while right in visit and visit[right] != True:
                visit[right] = True
                right += 1
                seq += 1
            res = max(res, seq)
        return res
                