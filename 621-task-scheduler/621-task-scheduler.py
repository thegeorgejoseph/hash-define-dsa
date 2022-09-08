class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        maxHeap = [-c for c in freqs.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0 
        while maxHeap or queue:
            time += 1
            if not maxHeap:
                time = queue[0][1]
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append((cnt, time + n))
            if len(queue) > 0 and time == queue[0][1]:
                count, t = queue.popleft()
                heapq.heappush(maxHeap, count)
        return time
    


    

