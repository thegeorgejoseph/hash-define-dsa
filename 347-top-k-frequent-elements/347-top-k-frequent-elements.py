class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)
        maxHeap = []
        for item, freq in freqs.items():
            heapq.heappush(maxHeap, (-freq, item))
        res = []
        while maxHeap:
            _, el = heapq.heappop(maxHeap)
            res.append(el)
            if len(res) == k:
                return res
        return res