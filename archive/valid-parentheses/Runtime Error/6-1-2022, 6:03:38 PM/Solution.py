// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']': '['}
        stack = []
        for e in s:
            if e in ('(', '{', '['):
                stack.append(e)
            else:
                curr = stack.pop()
                if curr is None or curr != matches[e]:
                    return False
        return len(stack) == 0
                