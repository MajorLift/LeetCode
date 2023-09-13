// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []
        def backtrack(tmp = [], start = 0, remainder = target):
            if remainder == 0:
                output.append(tmp)
            if remainder > 0:
                for i in range(start, n):
                    backtrack(tmp + [candidates[i]], i, remainder - candidates[i])
        backtrack()
        return output        