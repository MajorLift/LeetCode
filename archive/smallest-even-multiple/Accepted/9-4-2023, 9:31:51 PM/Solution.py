// https://leetcode.com/problems/smallest-even-multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)