// https://leetcode.com/problems/logger-rate-limiter

class Logger:

    def __init__(self):
        self.lastseen = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastseen \
            or timestamp >= self.lastseen[message] + 10:
            self.lastseen[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)