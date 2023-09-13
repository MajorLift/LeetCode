// https://leetcode.com/problems/min-cost-to-connect-all-points

class PrimNode:
    def __init__(self, idx, key):
        self.idx = idx
        self.key = key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return "(idx: %s, key: %s)" % (self.idx, self.key)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set()
        dist = [PrimNode(0, 0)] + [PrimNode(i, +math.inf) for i in range(1, len(points))]
        
        cost = 0
        while dist:
            u = heappop(dist)
            mst.add(u.idx)
            cost += u.key
            dist_update = []
            while dist:
                v = heappop(dist)
                if v.idx not in mst:
                    w = self.manhattan(points[u.idx], points[v.idx])
                    if w < v.key:
                        v.key = w
                    heappush(dist_update, v)
            dist += dist_update
        return cost
    
    def manhattan(self, a, b):
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) + abs(y1 - y2)

