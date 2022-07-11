class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, False) 
            
        for num in nums:
            if cache[num]:
                continue
            seq = 1
            left = num - 1
            right = num + 1
            cache[num] = True
            while left in cache and seq < len(nums):
                if not cache[left]:
                    seq += 1
                    cache[left] = True
                    left -= 1
                else:
                    break
            
            while right in cache and seq < len(nums):
                if not cache[right]:
                    seq += 1
                    cache[right] = True
                    right += 1
                else:
                    break
            res= max(res, seq)
        return res
                
            
        # if not nums:
        #     return 0
        # original = set(nums)
        # visit = set()
        # i = 0
        # n = len(nums)
        # res = 0
        # while i < n:
        #     curr = nums[i]
        #     if curr in visit:
        #         continue
        #     visit.add(curr)
        #     leftCount = 0
        #     k = curr
        #     while k - 1 in original and k - 1 not in visit:
        #         visit.add(k)
        #         leftCount += 1
        #         k -= 1
        #     rightCount = 0
        #     k = curr
        #     while k + 1 in original and k + 1 not in visit:
        #         visit.add(k)
        #         rightCount += 1
        #         k += 1
        #     res = max(res, leftCount + rightCount + 1)
        # return res