class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heappush(adj[u], v)

        output = deque()
        def dfs(u):
            while adj[u]:
                dfs(heappop(adj[u]))
            output.appendleft(u)
        dfs('JFK')
        return output