// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [
            (-math.sqrt(point[0] ** 2 + point[1] ** 2), i) 
                for i, point in enumerate(points)
        ]
        heap = [dist[j] for j in range(k)]
        heapq.heapify(heap)
        [
            heapq.heappushpop(heap, (dist[i][0], i)) 
                for i in range(k, len(points)) 
                if dist[i][0] > heap[0][0]
        ]
        return [points[i] for (_, i) in heap]