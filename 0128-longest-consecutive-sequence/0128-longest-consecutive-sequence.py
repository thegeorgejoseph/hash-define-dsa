class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = {num : False for num in nums}
        res = 0
        for num in nums:
            if cache[num]: continue
            seq = 1
            right = num + 1
            while right in cache and cache[right] == False:
                seq += 1
                cache[right] = True
                right += 1
            left = num - 1
            while left in cache and cache[left] == False:
                seq += 1
                cache[left] = True
                left -= 1
            res = max(res, seq)
        return res
                