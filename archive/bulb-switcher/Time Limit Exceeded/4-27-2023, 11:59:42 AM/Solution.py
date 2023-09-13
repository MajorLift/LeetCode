// https://leetcode.com/problems/bulb-switcher

class Solution:
    def bulbSwitch(self, n: int) -> int:
        self.n = n
        return len([True for e in map(self.numToggles, list(range(1, n + 1))) if e % 2 == 1])

    def numToggles(self, k):
        cnt = 0
        for i in range(1, self.n + 1):
            if k % i == 0:
                cnt += 1
        return cnt