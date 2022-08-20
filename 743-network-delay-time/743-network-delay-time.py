class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append([w,v])
        
        time = 0
        minHeap = [[0,k]]
        visit = set()
        
        #the graph can be disconnected
        while minHeap and len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            time = max(time, cost)
            
            for neiCost, j in graph[i]:
                if j not in visit:
                    heapq.heappush(minHeap,[cost + neiCost, j])
        
        return time if len(visit) == n else -1