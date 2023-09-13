// https://leetcode.com/problems/amount-of-new-area-painted-each-day

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        worklog, visited = [], dict()
        for start, end in paint:
            work = 0
            while start < end:
                if start not in visited:
                    visited[start] = end
                    work += 1
                    start += 1
                else:
                    prevEnd = visited[start]
                    visited[start] = max(prevEnd, end)
                    start = prevEnd
            worklog.append(work)
        return worklog