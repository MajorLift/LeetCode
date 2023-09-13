// https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m, n = map(len, (source, target))
        srcidxmap = defaultdict(list)
        for i, char in enumerate(source):
            srcidxmap[char].append(i)

        cnt = prev = 0
        for char in target:
            if char not in srcidxmap:
                return -1
            idxs = srcidxmap[char]
            curr = bisect_left(idxs, prev + 1)
            if curr == len(idxs):
                prev = idxs[0]
                cnt += 1
            else:
                prev = idxs[curr]
        return cnt
