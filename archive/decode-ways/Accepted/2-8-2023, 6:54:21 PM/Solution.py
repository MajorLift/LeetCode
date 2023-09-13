// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        acc = prev = 1
        for i in range(1, len(s)):
            acc, prev = (acc if s[i] != "0" else 0) + (prev if 10 <= int(s[i - 1:i + 1]) <= 26 else 0), acc
        return acc