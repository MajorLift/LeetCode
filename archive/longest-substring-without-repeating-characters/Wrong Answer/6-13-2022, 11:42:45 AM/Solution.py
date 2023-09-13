// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlen = 0
        hashmap = {}
        for end in range(len(s)):
            if s[end] in hashmap:
                start = max(start, hashmap[s[start]] + 1)
            else:
                maxlen = max(maxlen, end + 1 - start)
                hashmap[s[end]] = end
        return maxlen