// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall('[a-zA-Z0-9]', s)
        return all(s[i].lower() == s[-(i + 1)].lower() for i in range(len(s) // 2))