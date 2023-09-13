// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        flattened = [e for row in matrix for e in row]
        idx = bisect_left(flattened, target)
        return idx < m * n and flattened[idx] == target