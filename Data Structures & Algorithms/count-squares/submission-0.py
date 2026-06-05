class CountSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points:
            if (x == px) or (y == py) or abs(px - x) != abs(py - y):
                continue
            else:
                res += self.freq[(x, py)] * self.freq[(px, y)]
        return res
