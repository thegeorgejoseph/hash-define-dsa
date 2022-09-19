class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []
        # maxheap, minheap
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        
        if self.lower and self.upper and -self.lower[0] > self.upper[0]:
            num = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, num)
        
        if len(self.lower) > 1 + len(self.upper):
            num = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, num)
        elif len(self.upper) > 1 + len(self.lower):
            num = -1 * heapq.heappop(self.upper)
            heapq.heappush(self.lower,num)
        
    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()