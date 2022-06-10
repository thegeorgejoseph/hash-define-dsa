class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = {}
        max_seq = 1
        for num in nums:
            cache[num] = cache.get(num,False)
        
        for num in nums:
            if cache[num]:
                continue
            seq = 1
            cache[num] = True
            left = num - 1
            right = num + 1
            while seq < len(nums) and left in cache:
                if not cache[left]:
                    seq += 1
                    cache[left] = True
                    left -= 1
                else:
                    break
            while seq < len(nums) and right in cache:
                if not cache[right]:
                    seq += 1
                    cache[right] = True
                    right += 1
                else:
                    break
            max_seq = max(max_seq, seq)
        return max_seq
                