class CountSquares:

    def __init__(self):
        self.points = []
        self.pntcount = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))
        self.pntcount[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.pntcount[(px, y)] * self.pntcount[(x, py)]
        return res
        
        
