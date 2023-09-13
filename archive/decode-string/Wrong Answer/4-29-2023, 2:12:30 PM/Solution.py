// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                decoded = ""
                while not stack[-1].isnumeric():
                    decoded = stack.pop() + decoded
                k = stack.pop()
                stack.append(decoded * int(k))
            elif char != "[":
                stack.append(char)
        return ''.join(stack)