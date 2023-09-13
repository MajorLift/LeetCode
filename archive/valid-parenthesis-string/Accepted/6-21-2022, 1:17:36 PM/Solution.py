// https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = openMax = 0
        
        for c in s:
            openMin += 1 if c == '(' else -1
            if openMin < 0:
                openMin = 0
                
            openMax += 1 if c == '(' or c == '*' else -1
            if openMax < 0:
                return False
            
        return openMin == 0
