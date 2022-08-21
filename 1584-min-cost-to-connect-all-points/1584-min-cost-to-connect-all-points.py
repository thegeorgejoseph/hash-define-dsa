class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i :[] for i in range(len(points))}
        #each point is represented by the index that they are in in the list
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        minHeap = [[0,0]] # -> [cost, node index]
        visit = set()
        cost = 0
        
        while len(visit) < len(points):
            dist, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            cost += dist
            
            for neiCost, j in graph[i]:
                if j not in visit:
                    heapq.heappush(minHeap, [neiCost, j])
                    
        return cost