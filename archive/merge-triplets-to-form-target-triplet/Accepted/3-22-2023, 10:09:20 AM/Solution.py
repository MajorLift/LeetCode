// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0
        for triplet in triplets:
            if all(p <= q for p, q in zip(triplet, target)):
                x, y, z = map(max, zip((x, y, z), triplet))
                if [x, y, z] == target:
                    return True
        return False