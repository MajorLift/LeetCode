// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n, m = map(len, (s, t))
        s_cnt, t_cnt = [0] * 26, [0] * 26
        for i in range(m):
            if i < n: s_cnt[ord(s[i]) - ord('a')] += 1
            t_cnt[ord(t[i]) - ord('a')] += 1
        for j in range(26):
            if s_cnt[j] < t_cnt[j]:
                return chr(j + ord('a'))
