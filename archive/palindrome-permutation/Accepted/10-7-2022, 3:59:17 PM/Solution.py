// https://leetcode.com/problems/palindrome-permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_freq_chars = set()
        for char in s:
            if char in odd_freq_chars:
                odd_freq_chars.remove(char)
            else:
                odd_freq_chars.add(char)
        return len(odd_freq_chars) < 2