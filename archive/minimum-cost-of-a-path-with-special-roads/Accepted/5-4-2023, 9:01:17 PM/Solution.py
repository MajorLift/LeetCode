// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        (xs, ys), (xt, yt) = start, target
        adj = defaultdict(dict)
        nodes = set(map(tuple, (start, target)))
        for x1, y1, x2, y2, w in specialRoads:
            adj[(x1, y1)][(x2, y2)] = min(adj[(x1, y1)].get((x2, y2), +inf), w)
            nodes.add((x1, y1))
            nodes.add((x2, y2))
        for p1, p2 in permutations(nodes, 2):
            w = self.getCost(p1, p2)
            adj[p1][p2] = min(adj[p1].get(p2, +inf), w)
            adj[p2][p1] = min(adj[p2].get(p1, +inf), w)
        
        dist = defaultdict(lambda: +inf)
        dist[(xs, ys)] = 0
        queue = [(xs, ys)]
        while queue:
            u = queue.pop()
            for v in adj[u]:
                if dist[u] + adj[u][v] < dist[v]:
                    dist[v] = dist[u] + adj[u][v]
                    queue.append(v)
        return dist[(xt, yt)]
        
    def getCost(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])