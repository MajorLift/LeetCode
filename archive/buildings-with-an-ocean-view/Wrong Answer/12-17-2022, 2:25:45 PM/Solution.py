// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        maxes = [heights[-1]]
        for i in range(n - 2, -1, -1):
            maxes.append(max(maxes[-1], heights[i]))
        maxes.reverse()
        return [i for i, height in enumerate(heights) if height >= maxes[i]]