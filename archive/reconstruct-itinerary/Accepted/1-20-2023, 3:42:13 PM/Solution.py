// https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        output = deque()
        def dfs(src):
            while adj[src]:
                dfs(adj[src].popleft())
            output.appendleft(src)
        dfs("JFK")
        return output