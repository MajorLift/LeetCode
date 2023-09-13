// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        permutations = set([s1[i:] + s1[:i] for i in range(n1)])
        for j in range(n2 - n1):
            if s2[j:j + n1] in permutations:
                return True
        return False