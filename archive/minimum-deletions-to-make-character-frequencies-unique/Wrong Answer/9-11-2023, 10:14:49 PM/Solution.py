// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = sorted(Counter(s).values(), reverse=True)
        ans = 0
        for i in range(1, len(cnt)):
            while cnt[i] >= cnt[i - 1] > 0:
                cnt[i] -= 1
                ans += 1
        return ans