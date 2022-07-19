class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * n for n in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            top1 = heapq.heappop(maxHeap)
            top2 = heapq.heappop(maxHeap)
            if top1 != top2:
                heapq.heappush(maxHeap, top1 - top2)
        return -1 * maxHeap[0] if len(maxHeap) == 1 else 0