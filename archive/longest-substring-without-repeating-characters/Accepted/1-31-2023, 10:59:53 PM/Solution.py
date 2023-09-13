// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = defaultdict(int)
        global_max = 0
        l = r = 0
        while r < n:
            while seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1
            else:
                seen[s[r]] += 1
                r += 1
            global_max = max(global_max, r - l)
        return global_max