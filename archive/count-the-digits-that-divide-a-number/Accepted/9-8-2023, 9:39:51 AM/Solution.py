// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        cnt = Counter(str(num))
        return sum(cnt[digit] for digit in cnt if not num % int(digit))