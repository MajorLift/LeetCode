// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, space: str, target: str) -> str:
        target = set([*target])
        if not target or not space or not target.issubset(set([*space])):
            return None

        s, n = len(target), len(space)
        global_min_len, global_min_idx = +math.inf, (-1, -1)
        win_chars = defaultdict(int)
        l = r = 0
        while r < n:
            while r < n and not target.issubset(win_chars.keys()):
                win_chars[space[r]] += 1
                r += 1
            while target.issubset(win_chars.keys()):
                if r - l + 1 < global_min_len:
                    global_min_len = r - l + 1
                    global_min_idx = (l, r)
                if win_chars[space[l]] > 0:
                    win_chars[space[l]] -= 1
                    if win_chars[space[l]] == 0:
                        del win_chars[space[l]]
                    l += 1

        if global_min_len < +math.inf:
            i, j = global_min_idx
            return space[i:j]
        return None
