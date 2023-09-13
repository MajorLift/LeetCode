// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0
        for a, b, c in triplets:
            if all(u <= v for u, v in zip((a, b, c), target)):
                x, y, z = max(a, x), max(b, y), max(c, z)
        return [x, y, z] == target