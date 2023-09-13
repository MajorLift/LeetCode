// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        ans, tmp = 0, num
        while tmp:
            if not num % (tmp % 10):
                ans += 1
            tmp //= 10
        return ans
