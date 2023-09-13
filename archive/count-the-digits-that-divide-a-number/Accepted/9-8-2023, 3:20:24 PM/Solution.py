// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        def digit_iter(num: int):
            while num:
                yield num % 10
                num //= 10
        return sum(not int(num % digit) for digit in digit_iter(num))