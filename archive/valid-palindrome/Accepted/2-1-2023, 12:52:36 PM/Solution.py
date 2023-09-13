// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalpha() or char.isnumeric()]
        return all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))