// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n, m = len(num1), len(num2)
        output = [0] * (n + m)
        for i, j in product(range(n - 1, -1, -1), range(m - 1, -1, -1)):
            mul = reduce(operator.mul, map(int, (num1[i], num2[j]))) + output[i + j]
            output[i + j] = mul % 10
            output[i + j - 1] += mul // 10
        output.pop()
        while output[0] == 0:
            output.pop(0)
        return ''.join(map(str, output))
        
        # n, m = len(n1), len(n2)
        # ans = [0] * (n + m)
        # for i in range(n):
        #     for j in range(m):
        #         pos = i + j
        #         curr = n1[i] * n2[j] + ans[pos]
        #         ans[pos] = curr % 10
        #         ans[pos + 1] += curr // 10
        # while ans[-1] == 0:
        #     ans.pop()
        # return "".join([str(num) for num in ans[::-1]])