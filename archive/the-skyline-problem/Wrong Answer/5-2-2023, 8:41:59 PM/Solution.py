// https://leetcode.com/problems/the-skyline-problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        intervals = []
        maxr = -inf
        for l, r, h in buildings:
            maxr = max(maxr, r)
            heappush(intervals, (l, h, 'LEFT'))
            heappush(intervals, (r, h, 'RIGHT'))
        
        output = [[0, 0]]
        pq, visited = [], set()
        for pos in range(maxr):
            while intervals and intervals[0][0] == pos:
                _, h, _type = heappop(intervals)
                if _type == 'LEFT':
                    heappush(pq, -h)
                if _type == 'RIGHT':
                    visited.add(h)
            while pq and -pq[0] in visited:
                heappop(pq)
            if pq and -pq[0] != output[-1][1]:
                output.append([pos, -pq[0]])
            if not pq and output[-1][1] != 0:
                output.append([pos, 0])
                visited = set()
        return output[1:] + [[maxr, 0]]