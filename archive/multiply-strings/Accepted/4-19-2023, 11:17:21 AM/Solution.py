// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n, m = len(num1), len(num2)
        output = deque([0] * (n + m - 1))

        for i, j in product(range(n - 1, -1, -1), range(m - 1, -1, -1)):
            mul = int(num1[i]) * int(num2[j]) + output[i + j]
            output[i + j] = mul % 10
            if i + j - 1 >= 0:
                output[i + j - 1] += mul // 10
            else:
                output.appendleft(mul // 10)
        while output[0] == 0:
            output.popleft()
        
        return ''.join(map(str, output))
