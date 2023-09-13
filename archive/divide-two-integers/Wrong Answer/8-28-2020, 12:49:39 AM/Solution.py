// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0
        sgn = 1
        arr = [dividend, divisor]
        for i,e in enumerate(arr):
            if e < 0:
                arr[i] = -e
                sgn = -sgn
        dividend = arr[0]
        divisor = arr[1]
             
        quotient = 0
        while True:
            if dividend < divisor:
                break
            elif dividend == divisor:
                quotient += 1
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