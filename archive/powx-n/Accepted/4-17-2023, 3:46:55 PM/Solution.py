// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.power(x, n) if n >= 0 else self.power(1 / x, -n)

    def power(self, x, n):
        if n == 0: return 1
        if n == 1: return x
        sqrt = self.power(x, n // 2)
        return sqrt * sqrt * self.power(x, n % 2)
