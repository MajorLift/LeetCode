// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))
        
        invertidx = defaultdict(list)
        for i, char in enumerate(source):
            invertidx[char].append(i)
        
        cnt = 1
        i = 0
        for char in target:
            if char not in invertidx:
                return -1
            curr = invertidx[char]
            j = bisect_left(curr, i)
            if j == len(curr):
                cnt += 1
                i = curr[0] + 1
            else:
                i = curr[j] + 1
        return cnt