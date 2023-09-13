// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        num = start = sum(int(d) ** 2 for d in str(n))
        while True:
            num = sum(int(d) ** 2 for d in str(num))
            if num == start:
                return False
            if num == 1:
                return True