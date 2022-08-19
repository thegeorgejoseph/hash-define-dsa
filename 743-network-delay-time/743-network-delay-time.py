class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([w,v])
        
        time = 0
        minHeap = [[0, k]]
        visit = set()
        
        while minHeap and len(visit) < n:
            travelTime, dest = heapq.heappop(minHeap)
            if dest in visit:
                continue
            
            visit.add(dest)
            time = max(time, travelTime)
            
            for neiCost, j in graph[dest]:
                if j not in visit:
                    heapq.heappush(minHeap, [neiCost + time, j])
        
        return time if len(visit) == n else -1