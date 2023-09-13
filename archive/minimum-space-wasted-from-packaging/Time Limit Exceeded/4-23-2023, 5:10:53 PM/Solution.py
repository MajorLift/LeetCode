// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(packages), len(boxes)
        packages = Counter(packages)
        maxp, minp = max(packages.keys()), min(packages.keys())
        if maxp > max(max(b) for b in boxes):
            return -1

        global_min = +inf
        for catalogue in boxes:
            catalogue.sort()
            if catalogue[-1] < minp:
                continue
            total = 0
            for size, cnt in packages.items():
                idx = bisect_left(catalogue, size)
                if idx == len(catalogue):
                    total = -1
                    break
                total += (catalogue[idx] - size) * cnt
            if total > -1:
                global_min = min(global_min, total)
        return global_min