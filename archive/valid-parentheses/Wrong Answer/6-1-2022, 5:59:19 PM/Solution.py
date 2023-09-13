// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']': '['}
        stack = []
        for e in s:
            if e in ('(', '{', '['):
                stack.append(e)
            else:
                if len(stack) == 0:
                    break
                elif matches[e] == stack[-1]:
                    stack.pop()
        return len(stack) == 0
                