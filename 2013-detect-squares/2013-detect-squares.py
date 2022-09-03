class DetectSquares:

    def __init__(self):
        self.points = []
        self.counter = defaultdict(int)

    def add(self, point: List[int]) -> None:
        px, py = point
        self.counter[(px,py)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for px, py in self.points:
            if abs(x- px) != abs(y - py) or px == x or py == y:
                continue
            count += self.counter[(px,y)] * self.counter[(x,py)]
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)