// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        sub = ""

        for e in s:
            if e not in sub:
                sub = e
            if len(sub) > maxlen:
                maxlen = len(sub)
            
        return maxlen
        
        