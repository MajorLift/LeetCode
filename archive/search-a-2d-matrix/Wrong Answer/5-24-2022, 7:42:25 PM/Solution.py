// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            i, j = pivot_idx // n, pivot_idx % n
            pivot_elem = matrix[i][j]
            if pivot_elem < target:
                right = pivot_idx - 1
            elif pivot_elem > target:
                left = pivot_idx + 1
            else:
                return True
        return False
                