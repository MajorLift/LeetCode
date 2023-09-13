// https://leetcode.com/problems/break-a-palindrome

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        if all([char == "a" for char in palindrome]):
            return palindrome[:-1] + "b"
        for i, char in enumerate(palindrome):
            if char != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]                