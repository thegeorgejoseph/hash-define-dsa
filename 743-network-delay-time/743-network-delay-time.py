class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        minHeap = [[0,k]]
        time = 0
        visit = set()
        
        for u,v,c in times:
            graph[u].append([c,v])
        
        while minHeap and len(visit) < n:
            minCost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            time = max(time, minCost)
            
            for cost, j in graph[i]:
                if j not in visit:
                    heapq.heappush(minHeap, [cost + minCost, j])
        
        return time if len(visit) == n else -1