class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        maxHeap = []
        for n, cnt in freq.items():
            heapq.heappush(maxHeap,(-cnt, n))
        res = []
        while maxHeap:
            _, n = heapq.heappop(maxHeap)
            res.append(n)
            if len(res) == k:
                break
        return res