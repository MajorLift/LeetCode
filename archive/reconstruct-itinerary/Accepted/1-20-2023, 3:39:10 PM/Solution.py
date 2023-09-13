// https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        START = "JFK"
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
            adj[src].sort(reverse=True)

        output = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            output.append(src)
        dfs(START)
        return output[::-1]