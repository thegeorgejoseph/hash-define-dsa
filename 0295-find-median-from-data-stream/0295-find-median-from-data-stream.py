class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        
        if self.lower and self.upper and -1 * self.lower[0] > self.upper[0]:
            top = -1* heapq.heappop(self.lower)
            heapq.heappush(self.upper, top)
        if len(self.lower) -  len(self.upper) > 1:
            top = -1* heapq.heappop(self.lower)
            heapq.heappush(self.upper, top)
        elif len(self.upper) - len(self.lower) > 1:
            top = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -top)
        

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (-self.lower[0] + self.upper[0]) / 2
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return self.upper[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()