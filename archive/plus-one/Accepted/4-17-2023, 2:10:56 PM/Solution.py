// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last, rest = digits[-1], digits[:-1]
        if last < 9:
            return rest + [last + 1]
        elif not rest:
            return [1, 0]
        else:
            return self.plusOne(rest) + [0]
            
                
            