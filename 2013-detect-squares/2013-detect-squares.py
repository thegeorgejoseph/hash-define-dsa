class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        px, py = point
        self.counter[(px,py)] += 1
        self.points.append((px,py))

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px-x) != abs(py-y) or px == x or py == y:
                continue
            res += self.counter[(px,y)] * self.counter[(x, py)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)