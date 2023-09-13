// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b > 0:
            a, b = a ^ b, (a & b) << 1
        return a
