// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        num, numset = n, set()
        while True:
            if num == 1:
                return True
            num = sum(int(d) ** 2 for d in str(num))
            if num in numset:
                return False
            numset.add(num)
