// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def atoi(self, str) -> int:
        return str if int(str) == str \
            else int(str) if str[0] != '-' \
            else -1 * int(str[1:])
    
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            curr = tokens.pop()
            if curr.isnumeric() \
                or curr[0] == "-" and curr[1:].isnumeric():
                tokens.append(curr)
            else:
                y, x = self.atoi(tokens.pop()), self.atoi(tokens.pop())
                if curr == '+':
                    tokens.append(x + y)
                elif curr == '-':
                    tokens.append(x - y)
                elif curr == '*':
                    tokens.append(x * y)
                elif curr == '/':
                    tokens.append(int(x / y))
        return tokens.pop()