// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        digits[-1] = 0
        for i in range(0, len(digits)-1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            if i > 0:
                digits[i-1] += 1
            else:
                return [1] + [0 for _ in range(len(digits))]
        return digits
                