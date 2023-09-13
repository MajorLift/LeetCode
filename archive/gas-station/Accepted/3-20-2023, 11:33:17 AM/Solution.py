// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        stations = list(zip(gas, cost))
        total = tank = start = 0
        for i in range(n):
            g, c = stations[i]
            total += g - c
            tank += g - c
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1