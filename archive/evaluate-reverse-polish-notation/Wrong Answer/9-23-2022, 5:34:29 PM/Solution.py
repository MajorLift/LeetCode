// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", '/')
        tokens = [int(x) if x not in operators else x for x in tokens]
        stack = [tokens[0]]
        for token in tokens[1:]:
            if token not in operators:
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                curr = 0
                if token == "+":
                    curr = a + b
                if token == "-":
                    curr = a - b
                if token == "*":
                    curr = a * b
                if token == "/":
                    curr = a // b
                stack.append(curr)
        return stack.pop()