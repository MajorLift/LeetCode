// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        budget = list(zip(gas, cost))
        for start in range(n):
            if gas[start] == 0:
                continue
            tank = 0
            for offset in range(n):
                g, c = budget[(start + offset) % n]
                tank = tank + g - c
                if tank < 0:
                    break
            if tank >= 0:
                return start
        return -1
