// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (s[i] == s[-(i + 1)] for i in range(len(s)))