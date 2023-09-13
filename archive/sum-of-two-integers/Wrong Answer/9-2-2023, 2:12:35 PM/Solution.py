// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:

        def to_string(x):
            output = bin(x)[2:].rjust(12, '0')
            return output if x >= 0 else negate(output)

        def to_binary(bin_str):
            return int(bin_str, 2)

        def negate(bin_str):
            return ''.join(['0' if e == '1' else '1' for e in bin_str])

        def count_ones(x):
            cnt = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt

        def add(a, b):
            output = list(a)
            add = carry = 0
            for i in range(11, -1, -1):
                x, y = map(int, (a[i], b[i]))
                flag = 0
                flag |= carry << 2
                flag |= x << 1
                flag |= y << 0
                one_cnt = count_ones(flag)
                add, carry = one_cnt & (1 << 0), one_cnt & (1 << 1)
                output[i] = add
            return ''.join([str(e) for e in output])

        if a < 0 and b < 0:
            x, y = map(to_string, (-a, -b))
            is_neg = True
        else:
            x, y = map(to_string, (a, b))
            is_neg = False
        res = add(x, y)
        if res[0] == '1' and (a < 0 or b < 0):
            is_neg = True
            res = negate(res)
        return (-1 if is_neg else 1) * to_binary(res)
