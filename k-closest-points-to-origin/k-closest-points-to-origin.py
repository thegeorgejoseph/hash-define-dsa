class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            heapq.heappush(minHeap, (x**2 + y ** 2, x,y))
        res = []
        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            if len(res) == k:
                return res
        
            