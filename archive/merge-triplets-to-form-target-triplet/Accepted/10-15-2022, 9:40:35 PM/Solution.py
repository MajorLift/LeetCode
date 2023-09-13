// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                x, y, z = max(a, x), max(b, y), max(c, z)
        return [x, y, z] == target