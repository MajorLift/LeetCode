// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def atoi(self, str) -> int:
        return str if int(str) == str \
            else int(str) if str[0] != '-' \
            else -1 * int(str[1:])
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for curr in tokens:
            if curr.isnumeric() \
                or curr[0] == "-" and curr[1:].isnumeric():
                stack.append(curr)
            else:
                y, x = self.atoi(stack.pop()), self.atoi(stack.pop())
                if curr == '+':
                    stack.append(x + y)
                elif curr == '-':
                    stack.append(x - y)
                elif curr == '*':
                    stack.append(x * y)
                elif curr == '/':
                    stack.append(x // y + (0 if x / y - x // y < 0.5 else 1))
        return stack.pop()