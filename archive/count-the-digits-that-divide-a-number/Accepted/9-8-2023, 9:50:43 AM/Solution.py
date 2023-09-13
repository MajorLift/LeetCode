// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for digit in str(num) if not num % int(digit))