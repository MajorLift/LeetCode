// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                decoded = ""
                while not stack[-1].isnumeric():
                    decoded = stack.pop() + decoded
                count = ""
                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count
                stack.append(decoded * int(count or 1))
            elif char != "[":
                stack.append(char)
        return ''.join(stack)