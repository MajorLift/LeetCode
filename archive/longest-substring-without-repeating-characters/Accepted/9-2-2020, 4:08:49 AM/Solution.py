// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        sub = ""

        for i,e in enumerate(s):
            if e not in sub:
                sub += e
            else:
                j = self.findLastOccurrence(e, s[:i])
                sub = s[j+1:i+1]
                
            if len(sub) > maxlen:
                maxlen = len(sub)
            
        return maxlen
        
    def findLastOccurrence(self, char: str, s: str) -> int:
        for i in range(1,len(s)+1):
            if s[len(s)-i] == char:
                return len(s)-i
        return -1