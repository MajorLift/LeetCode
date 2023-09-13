// https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i, open_cnt):
            if open_cnt < 0:
                return False
            if i == len(s):
                return open_cnt == 0
            
            if s[i] == '(':
                return dp(i + 1, open_cnt + 1)
            elif s[i] == ')':
                return dp(i + 1, open_cnt - 1)
            else:
                return dp(i + 1, open_cnt - 1) \
                    or dp(i + 1, open_cnt) \
                    or dp(i + 1, open_cnt + 1)

        return dp(0, 0)
            