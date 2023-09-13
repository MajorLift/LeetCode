// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = ["" for _ in range(numRows)]
        unit = numRows + numRows - 2
        for i, char in enumerate(s):
            idx = i % unit
            if idx < numRows:
                mat[idx] += char
            else:
                mat[-(2 + idx % numRows)] += char
        return "".join(mat)