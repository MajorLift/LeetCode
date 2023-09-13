// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0: return 1.0
            sqrt = power(x, n // 2)
            if n % 2 == 0:
                return sqrt * sqrt
            return sqrt * sqrt * x

        return power(x, n) if n >= 0 else power(1 / x, -n)
