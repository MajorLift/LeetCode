// https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = defaultdict(list)
        for [src, dst] in tickets:
            flightMap[src].append(dst)
        flightMap = {k: deque(sorted(v)) for k, v in flightMap.items()}
        # print(flightMap)
        output = ["JFK"]
        curr = "JFK"
        while True:
            # print(curr)
            if curr in flightMap and len(flightMap[curr]):
                curr = flightMap[curr].popleft()
                output.append(curr)
            else:
                return output
            
        