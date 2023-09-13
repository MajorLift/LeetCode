// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        TARGET = "balloon"
        n, m = map(len, (text, TARGET))
        if n < m: 
            return 0
        
        cnt = 0
        balloon_cnt, window_cnt = Counter(TARGET), Counter(text[:m - 1])
        for i in range(m - 1, n):
            window_cnt[text[i]] += 1
            if all(balloon_cnt[k] <= window_cnt[k] for k in balloon_cnt):
                cnt += min(window_cnt[k] // balloon_cnt[k] for k in balloon_cnt)
                for k in balloon_cnt.keys():
                    window_cnt[k] -= 1
        return cnt
        