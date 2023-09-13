// https://leetcode.com/problems/reconstruct-itinerary

from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for depart, arrive in tickets:
            adj[depart].append(arrive)
        flights = {k: sorted(v, reverse=True) for k, v in adj.items()}

        output = []
        def dfs(depart):
            if depart in flights:
                stack = flights[depart]
                while stack:
                    dfs(stack.pop())
            output.append(depart)
        dfs('JFK')
        return output[::-1]