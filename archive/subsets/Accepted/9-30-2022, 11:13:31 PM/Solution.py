// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        def backtrack(tmp: List[int], start: int) -> None:
            nonlocal output
            output.append(tmp)
            for i in range(start, n):
                backtrack(tmp + [nums[i]], i + 1)
        backtrack([], 0)
        return output