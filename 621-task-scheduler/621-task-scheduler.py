class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxheap = [-c for c in counts.values()]
        heapq.heapify(maxheap)
        queue = deque()
        time = 0
        while maxheap or queue:
            time += 1
            if not maxheap:
                time = queue[0][1]
            if maxheap:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    queue.append([count, time + n])
            if queue and time == queue[0][1]:
                cnt = queue.popleft()[0]
                heapq.heappush(maxheap, cnt)
        return time
