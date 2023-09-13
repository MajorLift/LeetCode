// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = len(source), len(target)
        if set(source) < set(target):
            return -1

        @cache
        def dp(start):
            if start == m:
                return 0
            return min([1 + dp(i) 
                for i in range(start + 1, m + 1)
                if issubseq(target[start:i], source)] or [+inf])

        @cache
        def issubseq(s, t):
            if not s:
                return True
            if not t:
                return False
            for i in range(len(t)):
                if s[0] == t[i]:
                    return issubseq(s[1:], t[i+1:])
            return False

        res = dp(0)
        return res if res < +inf else -1