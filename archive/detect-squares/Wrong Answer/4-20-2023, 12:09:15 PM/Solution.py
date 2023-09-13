// https://leetcode.com/problems/detect-squares

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        x0, y0 = point
        for x, y in self.points:
            xdist, ydist = abs(x - x0), abs(y - y0)
            if xdist == ydist \
                and (x, y0) in self.points \
                and (x0, y) in self.points:
                cnt += self.points[(x, y)] * self.points[(x0, y)] * self.points[(x, y0)]
        return cnt


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)