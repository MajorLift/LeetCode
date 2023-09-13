// https://leetcode.com/problems/time-needed-to-inform-all-employees

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = 0
        tree = defaultdict(list)
        for employee, superior in enumerate(manager):
            if employee == headID: continue
            tree[superior].append(employee)
        queue = [headID]
        while queue:
            nxt_queue = []
            level_max = -inf
            for curr in queue:
                level_max = max(level_max, informTime[curr])
                nxt_queue.extend(tree[curr])
            ans += level_max
            queue = nxt_queue
        return ans