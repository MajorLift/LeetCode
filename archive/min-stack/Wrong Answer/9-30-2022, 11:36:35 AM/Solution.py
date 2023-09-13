// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.tracker and self.stack[-1] <= val:
            self.tracker[-1][1] += 1
        else:
            self.tracker.append([val, 1])

    def pop(self) -> None:
        self.stack.pop()
        if self.tracker[-1][1] == 0:
            self.tracker.pop()
        self.tracker[-1][1] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()