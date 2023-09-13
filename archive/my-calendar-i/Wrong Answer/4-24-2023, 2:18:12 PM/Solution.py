// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        l, r = bisect_right(self.cal, start), bisect_left(self.cal, end)
        if l % 2 == 0 and r % 2 == 0:
            self.cal[l:r] = [start, end]
            return True
        else:
            return False
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)