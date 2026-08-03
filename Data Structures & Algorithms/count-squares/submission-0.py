from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.pcount = defaultdict(int)
        self.temp = []


    def add(self, point: List[int]) -> None:
        self.pcount[tuple(point)] += 1
        self.temp.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.temp:
            if (abs(py-y) != abs(px-x) or x == px or y == py):
                continue
            res += self.pcount[(x, py)] * self.pcount[(px, y)]
        
        return res

