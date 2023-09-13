// https://leetcode.com/problems/parallel-courses-iii

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqs = [[] for _ in range(n)]
        for prereq, course in relations:
            prereqs[course - 1].append(prereq - 1)
        @cache
        def dp(node):
            return time[node] + max([0] + [dp(prereq) for prereq in prereqs[node]])
        return max(dp(node) for node in range(n))