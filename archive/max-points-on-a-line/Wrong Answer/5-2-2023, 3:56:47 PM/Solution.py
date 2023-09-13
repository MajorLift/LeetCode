// https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        hashmap = defaultdict(lambda: defaultdict(set))
        for (x1, y1), (x2, y2) in combinations(points, 2):
            a = -inf
            if x1 == x2:
                a = +inf
            elif y1 == y2:
                a = 0
            else:
                a = abs(x1 - x2) / abs(y1 - y2)
            b = y1 - a * x1
            hashmap[a][b].add((x1, y1))
            hashmap[a][b].add((x2, y2))
        ans = -inf
        for ka, va in hashmap.items():
            for kb, vb in va.items():
                ans = max(ans, len(vb))
        return ans