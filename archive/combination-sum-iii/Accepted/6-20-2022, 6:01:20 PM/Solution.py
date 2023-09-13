// https://leetcode.com/problems/combination-sum-iii

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                output.append(comb)
                return
            elif remain < 0 or len(comb) >= k:
                return
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain - (i + 1), comb[::], i + 1)
                comb.pop()
        backtrack(n, [], 0)
        return output