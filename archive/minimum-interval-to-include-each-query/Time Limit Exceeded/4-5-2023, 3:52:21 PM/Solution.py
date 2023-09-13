// https://leetcode.com/problems/minimum-interval-to-include-each-query

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for query in queries:    
            pq = []
            for l, r in intervals:
                if l <= query <= r:
                    heappush(pq, r - l + 1)
            output.append(pq[0] if pq else -1)
        return output
            
    