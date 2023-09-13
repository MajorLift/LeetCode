// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_cnt, window_cnt = Counter("balloon"), Counter(text)
        return min(window_cnt[k] // balloon_cnt[k] for k in balloon_cnt)
        