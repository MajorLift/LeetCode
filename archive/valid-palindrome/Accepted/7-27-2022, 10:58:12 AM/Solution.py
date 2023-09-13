// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""
        for char in s:
            if char.isalnum():
                s_alpha += char.lower()
        print(s_alpha)
        return all(s_alpha[i] == s_alpha[-(i + 1)] for i in range(len(s_alpha) // 2))