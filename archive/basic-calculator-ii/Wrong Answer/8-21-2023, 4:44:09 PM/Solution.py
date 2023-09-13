// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        tokens = []
        for char in s:
            if char == " ":
                continue
            elif char.isnumeric() and tokens and tokens[-1].isnumeric():
                tokens[-1] += char
            else:
                tokens.append(char)
        tokens = [int(token) if token.isnumeric() else token for token in tokens]

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