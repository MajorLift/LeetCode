// https://leetcode.com/problems/basic-calculator-iii

class Solution:
    def calculate(self, s) -> int:
        self.OPERATORS = set(["+", "-", "*", "/"])
        self.PARENS = set(["(", ")"])
        self.TOKENS = self.OPERATORS | self.PARENS

        exp = self.parse(s)
        paren_stack = []
        r = 0
        while r < len(exp):
            if exp[r] == "(":
                paren_stack.append(r)
            elif exp[r] == ")":
                l = paren_stack.pop()
                exp[l:r+1] = [self.eval_expression(exp[l+1:r])]
                r = l
            r += 1
        return self.eval_expression(exp)

    def parse(self, exp):
        output = []
        for char in exp:
            if char not in self.TOKENS:
                if not output or output[-1] in self.TOKENS:
                    output.append(char)
                elif output[-1] not in self.TOKENS:
                    output[-1] += char
            else:
                if output[-1] not in self.TOKENS:
                    output[-1] = int(output[-1])
                output.append(char)
        if output[-1] not in self.TOKENS:
            output[-1] = int(output[-1])
        return output
        
    def eval_expression(self, exp):
        op_stack, num_stack = [], []
        for elem in exp:
            if elem in self.OPERATORS:
                op_stack.append(elem)
            else:
                if op_stack and op_stack[-1] in ("*", "/"):
                    op, num = op_stack.pop(), num_stack.pop()
                    if op == "*":
                        num_stack.append(num * elem)
                    if op == "/":
                        num_stack.append(num // elem)
                else:
                    num_stack.append(elem)
        
        while len(num_stack) > 1:
            y, x = num_stack.pop(), num_stack.pop()
            op = op_stack.pop()
            if op == "+":
                num_stack.append(x + y)
            if op == "-":
                num_stack.append(x - y)

        return num_stack.pop()