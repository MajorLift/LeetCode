// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        packages.sort()
        boxes = [sorted(catalogue) for catalogue in boxes]
        if packages[-1] > max(max(b) for b in boxes):
            return -1
        global_min = +inf
        for catalogue in boxes:
            wasted = 0
            for size in packages:
                idx = bisect_left(catalogue, size)
                if idx == len(catalogue):
                    continue
                wasted += catalogue[idx] - size
            global_min = min(global_min, wasted)
        return global_min % MOD