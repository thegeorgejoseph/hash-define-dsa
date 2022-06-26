class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N): # we do not have to check whats behind because we are appending both directions in one go! Smart!
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
                
        
        cost = 0
        visit = set()
        frontier = [[0,0]]
        heapq.heapify(frontier)
        
        while len(visit) < N:
            curCost, i = heapq.heappop(frontier)
            if i in visit:
                continue
            
            visit.add(i)
            cost += curCost
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(frontier, [neiCost, nei])
        
        return cost