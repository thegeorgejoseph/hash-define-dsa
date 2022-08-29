class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x1, y1 in points:
            dist = x1**2  + y1**2
            heapq.heappush(minHeap,[dist, x1, y1])
        while minHeap:
            top = heapq.heappop(minHeap)
            res.append([top[1],top[2]])
            if len(res) == k:
                return res
        return res
