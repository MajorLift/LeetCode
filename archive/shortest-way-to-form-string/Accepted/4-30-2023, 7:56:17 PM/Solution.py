// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))
        if set(target) - set(source):
            return -1
        
        invertidx = defaultdict(list)
        for i, char in enumerate(source):
            invertidx[char].append(i)
        
        cnt = 1
        prev = -1
        for char in target:
            idxs = invertidx[char]
            curr = bisect_left(idxs, prev + 1)
            if curr < len(idxs):
                prev = idxs[curr]
            else:
                prev = idxs[0]
                cnt += 1
        return cnt