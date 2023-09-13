// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(tmp = [], start = 0, remainder = target):
            if remainder == 0:
                output.append(tmp)
            [backtrack(tmp + [candidates[i]], i, remainder - candidates[i]) for i in range(start, len(candidates))]
        backtrack()
        return output