// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        maxlen = 0
        hashmap = {}
        while end < len(s):
            if s[end] in hashmap:
                start = max(start, hashmap[s[start]] + 1)
            else:
                maxlen = max(maxlen, end - start + 1)
                hashmap[s[end]] = end
            print (start, end, hashmap)
            end += 1
        return maxlen