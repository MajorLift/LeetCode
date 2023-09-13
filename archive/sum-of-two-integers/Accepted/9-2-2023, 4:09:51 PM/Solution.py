// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask = (1 << 33) - 1 

        def to_binary(s):
            return int(s, 2)

        def to_string(x):
            output = bin(x)[2:].rjust(32, '0')
            return output if x >= 0 else negate(output)

        def negate(s):
            i = len(s) - 1
            while i >= 0 and s[i] == '0':
                i -= 1
            if i == -1: return ''.rjust(32, '0')
            return ''.join(['0' if e == '1' else '1' for e in s[:i]] + [s[i:]])

        def count_ones(x):
            cnt = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt

        def add(a, b):
            output = list(a)
            add = carry = 0
            for i in range(31, -1, -1):
                x, y = map(int, (a[i], b[i]))
                flag = 0
                flag |= carry << 2
                flag |= x << 1
                flag |= y << 0
                one_cnt = count_ones(flag)
                add, carry = one_cnt & (1 << 0), one_cnt & (1 << 1)
                output[i] = add
            return ''.join([str(e) for e in output])

        x, y = map(to_string, (a, b))
        res = add(x, y)
        return to_binary(res) if res[0] == '0' else -1 * to_binary(negate(res))
