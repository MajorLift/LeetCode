// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        if max(packages) > max(max(b) for b in boxes):
            return -1

        global_min = +inf
        for catalogue in boxes:
            catalogue.sort()
            wasted = 0
            for size in packages:
                idx = bisect_left(catalogue, size)
                if idx == len(catalogue):
                    wasted = -1
                    break
                wasted += catalogue[idx] - size
            if wasted > -1:
                global_min = min(global_min, wasted)
        return global_min % MOD