// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(start = 1, path = []):
            if len(path) == k:
                output.append(path)
            for num in range(start, n + 1):
                backtrack(num + 1, path + [num])
        backtrack()
        return output