// https://leetcode.com/problems/course-schedule-iii

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        for i, (duration, last_day) in enumerate(courses):
            heappush(pq, (last_day, duration, i))
        ans = 0
        d = 1
        while pq:
            while pq and pq[0][0] < d + pq[0][1]:
                heappop(pq)
            if not pq:
                break
            last_day, duration, i = heappop(pq)
            d += duration
            ans += 1
        return ans
