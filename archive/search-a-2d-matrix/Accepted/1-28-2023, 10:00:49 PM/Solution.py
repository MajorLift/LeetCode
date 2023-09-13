// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        idx = bisect_left([i for i in range(m * n)], target, key=lambda i: matrix[i // n][i % n])
        return idx < m * n and matrix[idx // n][idx % n] == target