// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for curr in tokens:
            if curr.isnumeric():
                stack.append(curr)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                if curr == '+':
                    stack.append(x + y)
                elif curr == '-':
                    stack.append(x - y)
                elif curr == '*':
                    stack.append(x * y)
                elif curr == '/':
                    stack.append(x // y)
        return stack.pop()