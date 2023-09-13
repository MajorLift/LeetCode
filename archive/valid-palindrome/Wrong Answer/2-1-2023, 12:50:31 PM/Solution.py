// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s if char.isalpha()]
        return all(s[i].lower() == s[-(i + 1)].lower() for i in range(len(s) // 2))