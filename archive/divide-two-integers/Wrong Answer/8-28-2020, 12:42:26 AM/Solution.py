// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0
        sgn = 0
        if dividend > 0 and divisor < 0:
            sgn = 1
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            sgn = 1
            dividend = -dividend     
        
        quotient = 0
        while True:
            if dividend <= divisor:
                break
            else:
                dividend -= divisor
                quotient += 1

        quotient = int(quotient)
        if sgn == 1:
            quotient = -quotient
        if quotient > 2**31 - 1 or quotient < -2**31:
            return 2**31 - 1
        else:
            return quotient