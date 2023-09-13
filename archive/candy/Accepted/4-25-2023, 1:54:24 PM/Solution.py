// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        memo = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                memo[i] = max(memo[i], memo[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                memo[i] = max(memo[i], memo[i + 1] + 1)
        return sum(memo)