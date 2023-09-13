// https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        close_acc, open_acc = list(accumulate([int(e == 'Y') for e in customers[::-1]]))[::-1] + [0], [0] + list(accumulate([int(e == 'N') for e in customers]))
        acc = list(map(sum, zip(close_acc, open_acc)))
        min_penalty, min_idx = +inf, -1
        for j in range(n + 1):
            if acc[j] < min_penalty:
                min_penalty, min_idx = acc[j], j
        return min_idx
            