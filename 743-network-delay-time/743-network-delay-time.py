class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([w,v])
         
        minHeap = [[0,k]] #0 time, k node
        heapq.heapify(minHeap)
        visit = set()
        res = 0
        
        while minHeap and len(visit) < n:
            time, node = heapq.heappop(minHeap)
            
            visit.add(node)
            res = max(res, time)
            
            for timeToNei, nei in graph[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,[time + timeToNei, nei])
        
        return res if len(visit) == n else -1