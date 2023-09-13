// https://leetcode.com/problems/course-schedule-ii

# [[1,0],[2,0],[3,1],[3,2]]
# adj_next: [[1, 2], [3], [3], []]
# adj_pre: [[], [0], [0], [1, 2]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # deserialize input into graph and also store in-degree
        adj_list = [[] for i in range(numCourses)]
        in_degrees = [0 for i in range(numCourses)]
        for [course, prereq] in prerequisites:
            adj_list[prereq].append(course)
            in_degrees[course] += 1
        
        # find starting points (0 in-degree) and add to queue
        queue = [course for course in range(numCourses) if in_degrees[course] == 0]
    
        # bfs
        path = []
        visited = [False for i in range(numCourses)]
        while len(queue) > 0 and len(path) < numCourses:
            curr = queue.pop(0)
            visited[curr] = True

            for course in adj_list[curr]:
                if visited[course] is False and in_degrees[course] > 0:
                    queue.append(course)
                    in_degrees[curr] -= 1
                    
            path.append(curr)
            
        return path