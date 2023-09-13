// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']': '['}
        stack = []
        for e in s:
            if e in ('(', '{', '['):
                stack.append(e)
            else:
                if len(stack) == 0 or stack.pop() != matches[e]:
                    return False
        return len(stack) == 0
                