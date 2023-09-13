// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))

        @cache
        def dp(start):
            if start == m:
                return 0
            local_min = +inf
            for i in range(start + 1, m + 1):
                if target[start:i] in all_subseqs:
                    local_min = 1 + min(local_min, dp(i))
            return local_min
        
        def subseqs(s):
            n = len(s)
            output = []
            for i in range(1, n + 1):
                output.extend(combinations(s, i))
            return set([''.join(e) for e in output])
                    
        all_subseqs = subseqs(source)
        print(all_subseqs)
        res = dp(0)
        return res if res < +inf else -1