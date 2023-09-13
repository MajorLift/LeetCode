// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))
        if set(target) - set(source):
            return -1

        @cache
        def dp(start):
            if start == m: return 0
            return min([1 + dp(i) 
                for i in range(start + 1, m + 1) 
                if issubseq(target[start:i])] 
                    or [+inf])

        @cache
        def issubseq(s):
            i = 0
            for char in source:
                if s[i] == char:
                    i += 1
                if i == len(s):
                    return True
            return False
                    
        res = dp(0)
        return res if res < +inf else -1