// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs, next_courses = [[] for i in range(numCourses)], [[] for i in range(numCourses)]
        for [course, prereq] in prerequisites:
            prereqs[course].append(prereq)
            next_courses[prereq].append(course)
            
        output = []
        queue = [course for course in range(numCourses) if len(prereqs[course]) == 0]
        while len(queue) > 0:
            curr = queue.pop(0)
            output.append(curr)
            queue.extend(next_courses[curr])
            
        return output if len(output) == numCourses else []