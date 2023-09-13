// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        return [i for i, height in enumerate(heights[:-1]) if height > max(heights[i+1:])] + [len(heights) - 1]