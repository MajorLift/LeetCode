// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits.pop() + 1
        if last == 10:
            return (self.plusOne(digits) if digits else [1]) + [0]
        return digits + [last]
