// https://leetcode.com/problems/sort-integers-by-the-power-value

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def dp(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + dp(x // 2)
            else:
                return 1 + dp(3 * x + 1)
        
        output = []
        for i in range(lo, hi + 1):
            output.append((dp(i), i))
        output.sort()
        return output[k - 1][1]
