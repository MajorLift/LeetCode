// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        prev = cnt = len([char for char in s[:k] if char in VOWELS])
        for r in range(k, len(s)):
            l = r - k + 1
            curr = prev \
                - (1 if s[l - 1] in VOWELS else 0) \
                + (1 if s[r] in VOWELS else 0)
            prev = curr
            cnt = max(cnt, curr)
        return cnt
            