// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        min_len, min_str = +inf, ""
        tcnt, window = Counter(t), defaultdict(int)
        while r < len(s):
            while r < len(s) and any(window[k] < tcnt[k] for k in tcnt):
                if s[r] in tcnt:
                    window[s[r]] += 1
                r += 1
            while all(window[k] >= tcnt[k] for k in tcnt):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_str = s[l:r]
                if s[l] in tcnt:
                    window[s[l]] -= 1
                l += 1
        return min_str
            