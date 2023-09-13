// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 1
        sub = ""

        for e in s:
            if e not in sub:
                sub += e
            else:
                if len(sub) > maxlen:
                    maxlen = len(sub)
                sub = e
            
        return maxlen
        
        