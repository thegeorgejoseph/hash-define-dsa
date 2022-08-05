class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        
        for diagX, diagY in self.points:
            if abs(px - diagX) != abs(py - diagY) or px == diagX or py == diagY:
                continue
            res += (self.counter[(px,diagY)] * self.counter[(diagX,py)])
        
        return res
