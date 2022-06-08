class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [e * -1 for e in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if first != second:
                heapq.heappush(maxHeap, first - second)
            
        if not maxHeap:
            return 0
        return -1 * maxHeap[0]