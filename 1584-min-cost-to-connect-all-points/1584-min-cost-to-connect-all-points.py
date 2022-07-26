class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        cost = 0
        minHeap = [[0,0]] # cost, node - the graph created above has a link between all possible nodes
        visit = set()
        
        while len(visit) < len(points):
            minCost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            cost += minCost
            
            for neiCost, nei in graph[i]:
                if nei not in visit:
                    heapq.heappush(minHeap,[neiCost, nei])
            
            
        return cost