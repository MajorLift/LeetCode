// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        charmap = {k: [chr(ord('a') + 3 * (k - 2) + i) for i in range(3)] for k in range(2, 7)}
        charmap[7] = [chr(ord('p') + i) for i in range(4)]
        charmap[8] = [chr(ord('t') + i) for i in range(3)]
        charmap[9] = [chr(ord('w') + i) for i in range(4)]

        output = []
        def backtrack(path = [], idx = 0):
            if idx == n:
                output.append(''.join(path))
                return
            for char in charmap[int(digits[idx])]:
                backtrack(path + [char], idx + 1)
        backtrack()
        return output
