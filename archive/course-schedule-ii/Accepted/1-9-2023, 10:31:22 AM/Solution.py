// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        output = []
        queue = collections.deque([i for i,e in enumerate(indegrees) if e == 0])
        while queue:
            curr = queue.popleft()
            output.append(curr)
            for course in adj[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return output if len(output) == numCourses else []