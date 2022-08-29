class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            if x == y:
                continue
            heapq.heappush(maxHeap, -1 * (abs(y) - abs(x)))
        return -maxHeap[0] if len(maxHeap) == 1 else 0