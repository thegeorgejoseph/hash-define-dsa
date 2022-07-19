class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            minHeap.append([x**2 + y**2, x, y])
        heapq.heapify(minHeap)
        while k > 0:
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res