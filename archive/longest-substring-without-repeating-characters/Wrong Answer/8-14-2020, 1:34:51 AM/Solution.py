// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        end = 1
        for i in range(1, len(s)-1):
            if start > end:
                for j in range(start, i):
                    if s[i] == s[j]:
                        end = i-1
                        if end - start + 1 > result:
                            result = end - start + 1
            else:
                if all([s[i] != s[j] for j in range(start, end+1)]):
                    start = i
        return result