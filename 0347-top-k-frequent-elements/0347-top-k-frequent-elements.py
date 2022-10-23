# heap solution - O(N) / O(N) spac
# bucket sort method - 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0 ) + 1
        for el, freq in cache.items():
            buckets[freq].append(el)
        for i in range(len(buckets)-1, -1, -1):
            for el in buckets[i]:
                res.append(el)
                if len(res) == k:
                    return res
        return res
                
            