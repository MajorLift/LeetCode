// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        local_max = global_max = 0
        for i in range(n):
            if s[i] in seen:
                seen = set([s[i]])
                local_max = 1
            else:
                seen.add(s[i])
                local_max += 1
                global_max = max(global_max, local_max)
        return global_max