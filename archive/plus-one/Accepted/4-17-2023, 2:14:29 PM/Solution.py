// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last, rest = digits[-1], digits[:-1]
        if last == 9:
            return (self.plusOne(rest) if rest else [1]) + [0]
        return rest + [last + 1]
        