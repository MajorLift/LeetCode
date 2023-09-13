// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        cnt = Counter(str(num))
        ans = 0
        for digit in cnt:
            if not num % int(digit):
                ans += cnt[digit]
        return ans