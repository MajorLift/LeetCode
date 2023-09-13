// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(packages), len(boxes)
        packages.sort()
        boxes = [sorted(catalogue) for catalogue in boxes]
        global_min = +inf
        for catalogue in boxes:
            wasted = 0
            for size in packages[::-1]:
                if size > catalogue[-1]:
                    wasted = -1
                    break
                wasted += catalogue[bisect_left(catalogue, size)] - size
            if wasted > -1:
                global_min = min(global_min, wasted)
        return global_min if global_min < +inf else -1