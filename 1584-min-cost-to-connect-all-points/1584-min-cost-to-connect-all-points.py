class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([distance, j])
                graph[j].append([distance, i])
        
        visit = set()
        minHeap = [[0,0]] # cost, index of point
        cost = 0
        
        while len(visit) < len(points):
            minDist, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            cost += minDist
            
            for neiCost, j in graph[i]:
                if j not in visit:
                    heapq.heappush(minHeap, [neiCost, j])
        
        return cost
        
        
        
        