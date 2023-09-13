// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        tokens = [int(char) if char.isnumeric() else char for char in s if char != " "]
        for i,e in enumerate(tokens):
            if e == "*":
                tokens[i-1:i+2] = [tokens[i - 1] * tokens[i + 1]]
            if e == "/":
                tokens[i-1:i+2] = [int(tokens[i - 1] / tokens[i + 1])]
        for i,e in enumerate(tokens):
            if e == "+":
                tokens[i-1:i+2] = [tokens[i - 1] + tokens[i + 1]]
            if e == "-":
                tokens[i-1:i+2] = [tokens[i - 1] - tokens[i + 1]]
        return tokens.pop()