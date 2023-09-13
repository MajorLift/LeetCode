// https://leetcode.com/problems/amount-of-new-area-painted-each-day

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        worklog, line = [0] * len(paint), defaultdict(int)
        for i, (start, end) in enumerate(paint):
            while start < end:
                jump = max(start + 1, line[start])
                worklog[i] += 1 if line[start] == 0 else 0
                line[start] = max(line[start], end)
                start = jump
        return worklog