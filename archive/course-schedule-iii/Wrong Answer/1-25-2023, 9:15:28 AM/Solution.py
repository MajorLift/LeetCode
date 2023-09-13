// https://leetcode.com/problems/course-schedule-iii

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses.sort(key=lambda x: x[1])
        pq = []
        ans = 0
        d = 0
        for i, (duration, last_day) in enumerate(courses):
            if d + duration <= last_day:
                heappush(pq, (duration, i))
                d += duration
                ans += 1
            elif pq and pq[0][0] > duration:
                duration_shorter, j = heappop(pq)
                d += duration - duration_shorter
                heappush(pq, (duration_shorter, j))
        return ans
