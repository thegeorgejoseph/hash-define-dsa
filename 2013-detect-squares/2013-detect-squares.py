class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.counter[(x,py)] * self.counter[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)