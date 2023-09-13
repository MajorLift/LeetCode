// https://leetcode.com/problems/single-threaded-cpu

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(start, duration, idx) for idx, [start, duration] in enumerate(tasks)]
        heapify(tasks)
        output, pq = [], []
        time = 0
        while tasks or pq:
            while tasks and tasks[0][0] <= time:
                start, duration, idx = heappop(tasks)
                heappush(pq, (duration, idx))
            if pq:
                duration, idx = heappop(pq)
                time += duration
                output.append(idx)
            else:
                time += tasks[0][0]
        return output
            