// https://leetcode.com/problems/course-schedule-iii

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        d = 0
        for i, (duration, last_day) in enumerate(courses):
            if d + duration <= last_day:
                heappush(pq, (-duration, i))
                d += duration
            elif pq and pq[0][0] < -duration:
                duration_longer, j = heappop(pq)
                duration_longer *= -1
                d += duration - duration_longer
                heappush(pq, (-duration_longer, j))
        return len(pq)
