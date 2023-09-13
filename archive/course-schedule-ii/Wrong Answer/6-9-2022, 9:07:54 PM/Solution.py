// https://leetcode.com/problems/course-schedule-ii

# [[1,0],[2,0],[3,1],[3,2]]
# adj_next: [[1, 2], [3], [3], []]
# adj_pre: [[], [0], [0], [1, 2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # deserialize input into graph
        adj_next, adj_pre = [[] for i in range(numCourses)], [[] for i in range(numCourses)]
        [(adj_pre[course].append(prereq), adj_next[prereq].append(course)) \
            for [course, prereq] in prerequisites]
        
        # find destination(s)
        queue = []
        for course, nexts in enumerate(adj_next):
            if len(nexts) == 0:
                queue.append(course)
        
        # bfs
        path = []
        visited = [False for i in range(numCourses)]
        while len(queue) > 0:
            # if all(course is True for course in visited):
            #     return []
            curr = queue.pop(0)
            if visited[curr] is False:
                visited[curr] = True
                path.append(curr)

            for course in adj_pre[curr]:
                if visited[course] is False:
                    queue.append(course)
        
        return path[::-1]