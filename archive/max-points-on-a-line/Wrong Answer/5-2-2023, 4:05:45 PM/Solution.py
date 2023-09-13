// https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: 
            return len(points)

        hashmap = defaultdict(lambda: defaultdict(set))
        for (x1, y1), (x2, y2) in combinations(points, 2):
            if x1 == x2: 
                a, b = +inf, nan
            elif y1 == y2: 
                a, b = 0, y1
            else: 
                a = (y1 - y2) / (x1 - x2)
                b = y1 - a * x1
            hashmap[a][b].add((x1, y1))
            hashmap[a][b].add((x2, y2))
            
        return max(len(vb) for va in hashmap.values() for vb in va.values())