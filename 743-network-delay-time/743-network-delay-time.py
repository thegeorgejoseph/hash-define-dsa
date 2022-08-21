class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append([w,v])
        
        minHeap = [[0,k]] # -> [cost, starting node]
        visit = set()
        res = 0
        
        while minHeap and len(visit) < n:
            time, dest = heapq.heappop(minHeap)
            if dest in visit:
                continue
            
            visit.add(dest)
            res = max(res, time)
            
            for neiTime, dst in graph[dest]:
                if dst not in visit:
                    heapq.heappush(minHeap,[neiTime + time, dst])
        
        return res if len(visit) == n else -1