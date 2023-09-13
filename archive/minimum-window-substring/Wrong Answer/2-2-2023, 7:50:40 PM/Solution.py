// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or not set([*t]).issubset(set([*s])):
            return ""

        n = len(s)
        min_len, min_idx = +math.inf, (-1, -1)
        window, target = defaultdict(int), Counter(t)
        print(target)
        l = r = 0
        while r < n:
            while r < n and len(window) < len(target):
                print(window)
                if s[r] in target:
                    window[s[r]] += 1
                r += 1
            
            while len(window) == len(target):
                print(window)
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_idx = (l, r)
                
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] <= 0:
                        del window[s[l]]
                l += 1

        if min_len < +math.inf:
            i, j = min_idx
            return s[i:j]
        return ""
