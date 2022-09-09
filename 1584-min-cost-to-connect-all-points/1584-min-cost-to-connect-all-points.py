class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                graph[i].append([dist, j])
                graph[j].append([dist,i])
        
        minHeap = [[0,0]] #0 cost start from 0th point in points
        heapq.heapify(minHeap)
        visit = set()
        res = 0
        while minHeap and len(visit) < len(points):
            cost, node = heapq.heappop(minHeap)
            if node in visit: continue
            visit.add(node)
            res += cost
            
            for neiCost, nei in graph[node]:
                heapq.heappush(minHeap,[neiCost, nei])
        
        return res if len(visit) == len(points) else 0