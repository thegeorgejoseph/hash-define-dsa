# heap solution - O(N) / O(N) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        maxHeap = []
        for el, freq in cache.items():
            heapq.heappush(maxHeap, (-freq, el))
        res = []
        while maxHeap:
            _, el = heapq.heappop(maxHeap)
            res.append(el)
            if len(res) == k:
                return res
        return res
        