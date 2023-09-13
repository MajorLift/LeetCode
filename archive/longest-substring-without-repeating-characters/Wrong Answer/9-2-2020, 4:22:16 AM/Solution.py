// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0
        sub = ""

        while right < len(s):
            if s[right] not in sub:
                sub += s[right]
                if len(sub) > maxlen:
                    maxlen = len(sub)
                right += 1
            else:
                sub = s[left+1:right+1]
                left += 1
            
        return maxlen