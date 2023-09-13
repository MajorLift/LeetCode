// https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and len(stack) and stack[-1] == '(' or char == '*':
                stack.pop()
        return len(stack) == 0