// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        forbidden = set()
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                forbidden.add((a, b, c))
        
        x, y, z = 0, 0, 0
        for a, b, c in triplets:
            if (a, b, c) not in forbidden:
                x, y, z = max(a, x), max(b, y), max(c, z)
        # print(x, y, z)
        return [x, y, z] == target