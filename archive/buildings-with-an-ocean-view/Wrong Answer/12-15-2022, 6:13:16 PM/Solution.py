// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        arr = heights[::-1]
        maxes = itertools.accumulate(arr, max)
        return [curr - 1 for local_max, curr in zip(maxes, arr) if curr >= local_max]