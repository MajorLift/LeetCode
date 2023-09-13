// https://leetcode.com/problems/detonate-the-maximum-bombs

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for i, j in product(range(n), range(n)):
            if i != j and self.inRange(bombs[i], bombs[j]):
                adj[i].append(j)
                indegree[j] += 1
        candidates = [i for i,e in enumerate(indegree) if e == 0]
        if not candidates:
            return n
            
        ans = 0
        for start in candidates:
            queue, visited = deque([start]), set([start])
            while queue:
                curr = queue.popleft()
                for v in adj[curr]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)
            ans = max(ans, len(visited))
        return ans
        
    def inRange(self, s, t):
        (x1, y1, r1), (x2, y2, _) = s, t
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2
