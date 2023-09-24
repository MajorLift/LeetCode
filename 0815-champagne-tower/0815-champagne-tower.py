class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[0] * k for k in range(1, 102)]
        memo[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                spill = max(0, (memo[i][j] - 1) / 2)
                memo[i + 1][j] += spill
                memo[i + 1][j + 1] += spill
        return min(1, memo[query_row][query_glass])