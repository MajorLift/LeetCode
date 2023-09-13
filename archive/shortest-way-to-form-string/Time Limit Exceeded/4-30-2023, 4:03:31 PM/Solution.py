// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))
        if set(target) - set(source):
            return -1

        memo = [+inf] * m + [0]
        def dp(start):
            if memo[start] < +inf:
                return memo[start]
            local_min = +inf
            for i in range(start + 1, m + 1):
                if issubseq(target[start:i]):
                    local_min = 1 + min(local_min, dp(i))
            memo[start] = local_min
            return memo[start]
        
        subseq_memo = set()
        def issubseq(s):
            if s in subseq_memo:
                return True
            i = 0
            for char in source:
                if s[i] == char:
                    i += 1
                if i == len(s):
                    subseq_memo.add(s)
                    return True
            return False
                    
        res = dp(0)
        return res if res < +inf else -1