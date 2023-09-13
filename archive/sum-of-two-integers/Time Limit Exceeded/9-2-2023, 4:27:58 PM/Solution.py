// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 33) - 1 
        while b:
            a, b = (a ^ b), ((a & b) << 1)
        return a & mask if a <= (mask >> 1) else ~(a ^ mask)