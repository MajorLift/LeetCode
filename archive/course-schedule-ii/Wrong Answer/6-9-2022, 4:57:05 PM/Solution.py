// https://leetcode.com/problems/course-schedule-ii

# [[1,0],[2,0],[3,1],[3,2]]
# adj_next: [[1, 2], [3], [3], []]
# adj_pre: [[], [0], [0], [1, 2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # deserialize input into graph
        adj_next, adj_pre = [[] for i in range(numCourses)], [[] for i in range(numCourses)]
        [(adj_pre[course].append(prereq), adj_next[prereq].append(course)) for [course, prereq] in prerequisites]
        # find a starting point
        start = None
        for course, prereqs in enumerate(adj_pre):
            if len(prereqs) == 0:
                # if there are multiple return []
                if start is not None:
                    return []
                else:
                    start = course
        if start is None:
            return []
        
        path = []
        visited = [False for i in range(numCourses)]
        stack = [start]
        # dfs ending when length of output array (path) is equal to numCourses
        while len(stack) > 0:
            # for each course, all of its prerequisites must be 'visited' before it can be traversed
            curr = stack.pop()
            visited[curr] = True
            
            for prereq in adj_next[curr]:
                if visited[prereq] is False:
                    stack.append(prereq)
            
            path.append(curr)
            
        return path
    