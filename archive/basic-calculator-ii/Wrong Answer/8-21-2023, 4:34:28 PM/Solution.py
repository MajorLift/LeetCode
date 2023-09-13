// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        tokens = [char for char in s if char != " "]
        for i, (a, b) in enumerate(zip(tokens, tokens[1:])):
            if a.isnumeric() and b.isnumeric():
                tokens[i:i+2] = [a + b]
        tokens = [int(char) if char.isnumeric() else char for char in tokens]
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