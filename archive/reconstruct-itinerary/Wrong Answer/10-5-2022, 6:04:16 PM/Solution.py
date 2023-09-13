// https://leetcode.com/problems/reconstruct-itinerary

from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for depart, arrive in tickets:
            adj[depart].append(arrive)
        adj = {k: deque(sorted(v)) for k, v in adj.items()}
        
        queue = deque(["JFK"])
        output = []
        while queue:
            curr = queue.popleft()
            output.append(curr)
            if curr in adj and len(adj[curr]):
                destination = adj[curr].popleft()
                queue.append(destination)
        return output