class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        minHeap = [[0,0]]
        heapq.heapify(minHeap)
        visit = set()
        total = 0
        while minHeap and len(visit) < len(points):
            cost, node = heapq.heappop(minHeap)
            if node in visit: continue
            total += cost
            visit.add(node)
            
            for neiCost, nei in graph[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return total if len(visit) == len(points) else 0