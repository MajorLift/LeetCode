// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1
        start = 0
        end = 0
        for i in range(1, len(s)-1):
            if start >= end and \
            any([s[i] == s[j] for j in range(start, i+1)]):
                end = i-1
                if end - start + 1 > result:
                    result = end - start + 1
            elif start < end and \
            all([s[i] != s[j] for j in range(start, end+1)]):
                start = i
        return result