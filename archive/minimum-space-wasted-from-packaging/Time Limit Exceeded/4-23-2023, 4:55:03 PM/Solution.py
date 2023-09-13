// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(packages), len(boxes)
        maxp, minp = max(packages), min(packages)
        if maxp > max(max(b) for b in boxes):
            return -1

        global_min = +inf
        for catalogue in boxes:
            catalogue.sort()
            if catalogue[-1] < minp:
                continue
            box_total = 0
            for size in packages:
                idx = bisect_left(catalogue, size)
                if idx >= len(catalogue):
                    box_total = -1
                    break
                box_total += catalogue[idx]
            if box_total > -1:
                global_min = min(global_min, box_total)
        return (global_min - sum(packages)) % MOD