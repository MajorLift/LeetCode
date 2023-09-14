class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[1] - x[0])
        return sum(costs[i][i < n] for i in range(2 * n))